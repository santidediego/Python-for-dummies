#!/usr/bin/env python3

# -*- coding:utf-8 -*-

from flask import Flask, session, redirect, url_for, escape, request, Response,render_template
from wtforms import Form, DateField, BooleanField, TextField, PasswordField, RadioField, validators
from mandelbrot import *

import dbm

import re

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')


bd = dbm.open('base_datos.dat', 'c')
#bd_name = dbm.open('base_datos_nombre.dat', 'c')
#bd_password = dbm.open('base_datos_contrasena.dat', 'c')

app =Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

__contador__=0
__first_time__=True
#path = '/home/neon_520/Dropbox/Facultad/DAI/p3/sesion'  

"""
Historial
"""
def quitarPrimero(lista):
    for j in range(2):
        lista[str(j)]=lista[str(j+1)]

def almacenar_historial(request):
    global __contador__
    global __first_time__
    if __contador__ == 2:
        if __first_time__:
            __first_time__=False
        else:
            quitarPrimero(session)
        session[str(__contador__)]=str(request.url)
    else:
        session[str(__contador__)]=str(request.url)
        __contador__+=1


def Sesiones_html():
    global __contador__
    ses_html=list()
    for j in range(0,__contador__+1):
        ses_html.append(session[str(j)])

    return ses_html

"""
Gestion de menus
"""

@app.route('/')
def index():
    almacenar_historial(request)
    return render_template('index.html')


@app.route("/P2")
def indexp2():
    almacenar_historial(request)
    return render_template('indexp2.html')

@app.route("/P3")
def indexp3():
    global __contador__
    almacenar_historial(request)
    if 'username' in session:
        logued=True
    else:
        logued=False
    return render_template('indexp3.html', logued=logued, sesiones=Sesiones_html())


"""
Practica 2
"""

@app.route('/P2/png')
def imagen():
    almacenar_historial(request)
    archivo=open("./png/imagen_png.png",'rb')
    #try:
    imagen_png=archivo.read()
    response = Response()
    response.headers.add('Content-Type', 'image/png')
    response.set_data(imagen_png)
    return response
    #except ValueError as e:
    #   return "Error" + str(e)

@app.route('/P2/user/<username>')
def mostrarPerfilUsuario(username):
    almacenar_historial(request)
    # Mostrar el perfil de usuario
    return 'Usuario %s' % username

@app.route('/P2/mandelbrot')
def mostrarMandelbrot():
    almacenar_historial(request)
    paleta=[[0,0,0],[100,100,100],[50,50,50]]
    x1=int(request.args.get('x1'))
    y1=int(request.args.get('y1'))
    x2=int(request.args.get('x2'))
    y2=int(request.args.get('y2'))
    renderizaMandelbrotBonito(x1, y1, x2, y2, 5000, 50, "archivo.png", paleta, 3)
    archivo=open("archivo.png",'rb')
    imagen_png=archivo.read()
    response = Response()
    response.headers.add('Content-Type', 'image/png')
    response.set_data(imagen_png)
    return response

@app.errorhandler(404)
def page_not_found(error):
    almacenar_historial(request)
    return "Pagina no encontrada "+str(404)


"""
Practica 3
"""

def esCorreo(form, field):
    if not re.match('\w+@(\w+)\.com|es',field.data):
        raise validators.ValidationError('Esto no es un correo electronico')

def esVISA(form, field):
    if not re.match('(((\d{4}-){3})|((\d{4} ){3}))\d{4}',field.data):
        raise validators.ValidationError('Esto no es una Tarjeta de credito')

def sonApellidos(form,field):
    if not re.match('\w+ \w+',field.data):
        raise validators.ValidationError('No has puesto tus apellidos')

def invalidPass(form,field):
    if bytes(form.username.data+'_password','utf-8') in bd:
        if not bd[form.username.data+'_password'] == bytes(field.data,'utf-8') :
            raise validators.ValidationError('Contraseña incorrecta')

def invalidUser(form,field):
    if not bytes(field.data+'_name','utf-8') in bd:
        raise validators.ValidationError('Usuario incorrecto')


class RegistrationForm(Form):
    username = TextField('Nombre', [
        validators.Required(),
        validators.Length(min=6, max=15)
    ])

    surnames = TextField('Apellidos', [
        validators.Required(),
        sonApellidos
    ])
    email = TextField('Dirección de email', [
        validators.Required(),
        esCorreo
    ])
    visa = TextField('VISA', [
        validators.Required(),
        esVISA
    ])

    fec = DateField('Fecha de Nacimiento', [
        validators.Required()
    ],  format='%d-%m-%Y')#aun falta la condicion de fecha correcta

    direccion = TextField('Dirección', [
        validators.Required()
    ])

    password = PasswordField('Contraseña', [
        validators.Required(),
        validators.EqualTo('confirm', message='La Contraseña debe coincidir con la repetición')
    ])
    confirm = PasswordField('Repite la Contraseña')

    pago = RadioField('Forma de pago', 
        choices=[('tipo1','VISA'),('tipo2','Contrareembolso')
    ])
    
    accept_tos = BooleanField('Acepto las condiciones', [validators.Required()])


class Login(Form):
    username = TextField('Nombre de Usuario', [
        validators.Length(min=6, max=15), 
        invalidUser,
        validators.Required()
    ])
    password = PasswordField('Contraseña', [
        validators.Required(),
        invalidPass
    ])



@app.route('/P3/register', methods=['GET', 'POST'])
def formulario():
    almacenar_historial(request)
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        bd[form.username.data+'_name']=form.username.data
        bd[form.username.data+'_surnames']=form.surnames.data
        bd[form.username.data+'_email']=form.email.data
        bd[form.username.data+'_fec']=str(form.fec.data)
        bd[form.username.data+'_direccion']=form.direccion.data
        bd[form.username.data+'_password']=form.password.data
        bd[form.username.data+'_pago']=form.pago.data

        return('Gracias %s por registrarte' % form.username.data)

    return render_template('register.html', form=form, sesiones=Sesiones_html())



@app.route('/P3/login', methods=['GET','POST'])
def login():
    almacenar_historial(request)
    form = Login(request.form)
    logued=False
    if 'username' in session: #Si hay una sesion activa
        logued=True
    elif request.method == 'POST' and form.validate():
        if not form.username.data in session:
            session['username']=form.username.data #meterlo en sesiones
            logued=True
        else:
            return('Sesión ya iniciada previamente')

    return render_template('login.html', form=form, logued=logued, sesiones=Sesiones_html())


"""
@app.route('/loguedin', methods=['GET','POST'])
def loguedin():
    form = loguedin(request.form)
    if request.method == 'POST' and form.validate():
        #app.session_interface.__setitem__(form.username.data,form.password.data)
        sesion.append(app.session_interface.open_session(app,request))
        return('Bienvenido %s' % form.username.data)

    return render_template('loguedin.html', form=form)
"""

@app.route('/P3/logout')
def logout():
    almacenar_historial(request)
    # remove the username from the session if it's there
    session.pop('username', None)
    Log=False
    return redirect('/P3')

@app.route('/visualizar')
def visualizar():
    pass


@app.route('/perfil')
def perfil():
    almacenar_historial(request)
    logued=False
    if 'username' in session: #Si hay una sesion activa
        logued=True
    
    return render_template('perfil.html', logued=logued, sesiones=Sesiones_html())


if __name__ == "__main__":
    app.debug=True
    app.run()