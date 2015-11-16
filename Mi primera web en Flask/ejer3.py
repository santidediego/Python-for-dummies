#!/usr/bin/env python

# -*- coding:utf-8 -*-

from flask import Flask, session, redirect, url_for, escape, request, Response,render_template
from wtforms import Form, DateField, BooleanField, TextField, PasswordField, RadioField, validators
from mandelbrot import *

import dbm

import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


bd_name = dbm.open('base_datos_nombre.dat', 'c')
bd_password = dbm.open('base_datos_contrasena.dat', 'c')

app =Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#path = '/home/neon_520/Dropbox/Facultad/DAI/p3/sesion'                     





"""
Gestion de menus
"""

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/P2")
def indexp2():
    return render_template('indexp2.html')

@app.route("/P3")
def indexp3():
    if 'username' in session:
        logued=True
    else:
        logued=False
    return render_template('indexp3.html', logued=logued)


"""
Practica 2
"""

@app.route('/P2/png')
def imagen():
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
    # Mostrar el perfil de usuario
    return 'Usuario %s' % username

@app.route('/P2/mandelbrot')
def mostrarMandelbrot():
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
    if form.username.data in bd_name:
        if not bd_password[form.username.data] == field.data :
            raise validators.ValidationError('Contrasena incorrecta')

def invalidUser(form,field):
    if not field.data in bd_name:
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
    email = TextField('Direccion de email', [
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

    direccion = TextField('Direccion', [
        validators.Required()
    ])

    password = PasswordField('Contrasena', [
        validators.Required(),
        validators.EqualTo('confirm', message='La contrasena debe coincidir con la repeticion')
    ])
    confirm = PasswordField('Repite la contrasena')
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
    password = PasswordField('Contrasena', [
        validators.Required(),
        invalidPass
    ])



@app.route('/P3/register', methods=['GET', 'POST'])
def formulario():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        bd_name[form.username.data]=form.username.data
        bd_password[form.username.data]=form.password.data
        return('Gracias %s por registrarte' % form.username.data)

    return render_template('register.html', form=form)



@app.route('/P3/login', methods=['GET','POST'])
def login():
    form = Login(request.form)
    logued=False
    if 'username' in session: #Si hay una sesion activa
        logued=True
    elif request.method == 'POST' and form.validate():
        #if form.username.data in bd_name:
        #    if bd_password[form.username.data] == form.password.data :
        if not form.username.data in session:
            session['username']=form.username.data #meterlo en sesiones
            logued=True
        else:
            return('Sesion ya iniciada previamente')
            #else:
             #   return('Contrasena incorrecta')
        #else:
            #return('Usuario no registrado')
        #    return redirect('/P3/register')

    return render_template('login.html', form=form, logued=logued)


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
def loguedout():
    # remove the username from the session if it's there
    session.pop('username', None)
    Log=False
    return redirect('/P3')

@app.route('/visualizar')
def visualizar():
    pass


@app.route('/perfil')
def perfil():
    logued=False
    if 'username' in session: #Si hay una sesion activa
        logued=True
    return render_template('perfil.html', logued=logued)


if __name__ == "__main__":
    app.debug=True
    app.run()