from flask import Flask
from flask import render_template,request,session, redirect, url_for,escape
#from flask.ext import shelve
#Este modulo es una extension de shelve, shelve ya viene por defecto aunque podemos usar esta también
from wtforms import Form, BooleanField, TextField, PasswordField, TextAreaField, SelectField, RadioField, DateField, validators
#Regexp es para validar expresiones regulares

import shelve
import dbm
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
__count__=0
__firstTime__=True
#Las dos siguientes sentencias sirven para que funcione shelve. Solo necesario si trabajamos con la extension
#app.config['SHELVE_FILENAME'] = 'shelve.db'
#shelve.init_app(app)

db = dbm.open('base_datos.dat', 'c')
db_datos = shelve.open('datos_usuarios','c') #Esta la usaremos para almacenar datos de usuarios

"""
Historial
-"""

def deleteFirst(lista):
    for i in range(2):
        lista[str(i)]=lista[str(i+1)]
def save_hist(request):
    global __count__
    global __firstTime__
    if __count__ == 2:
        if __firstTime__:
            __firstTime__=False
        else:
            deleteFirst(session)
        session[str(__count__)]=str(request.url)
    else:
        session[str(__count__)]=str(request.url)
        __count__+=1

def html_sessions():
    global __count__
    ses_html=list()
    for i in range(0,__count__):
        ses_html.append(session[str(i)])
    return ses_html

def PassWrong(form,field):
    if form.username.data in db:
        if not db[form.username.data] == bytes(field.data,'utf-8') :
            raise validators.ValidationError('Contraseña incorrecta')

def guardar_datos(form):
        lista=list()
        lista.append(str(form.DNI.data))
        lista.append(str(form.date.data))
        lista.append(str(form.email.data))
        lista.append(str(form.adress.data))
        lista.append(str(form.payment.data))
        lista.append(str(form.VISA.data))
        lista.append(str(form.password.data))
        db_datos[str(form.username.data)]=lista

class Login(Form):
    username = TextField('Nombre de Usuario', [validators.Length(min=4, max=25)])
    password = PasswordField('Contraseña', [
         validators.Required(),
         PassWrong
    ])

class Formulario2(Form):
    username = TextField('Nombre de Usuario', [validators.Length(min=4, max=25)])
    DNI = TextField('DNI', [validators.Length(min=9, max=9, message='Debe tener 9 caracteres')])
    date = DateField('Fecha de nacimiento', format='%d/%m/%Y')
    email = TextField('Dirección de email', [
            validators.Length(min=6, max=35),
            validators.Regexp(regex='\w+@(\w+)\.com|es',message='Dirección no válida')
    ])
    adress = TextAreaField('Dirección:',[validators.Length(min=1,max=50)])
    payment = RadioField('Forma de pago:' , choices=[('Efectivo','A contrarrembolso'),('Tarjeta','VISA')])
    VISA = TextField('VISA', [
            validators.Length(min=19, max=19, message="El número de tarjeta debe tener 16 caracteres"),
            validators.Regexp(regex='(\d{4}(-| )){3}\d{4}',message='Formato de tarjeta no válido')
    ])
    password = PasswordField('Contraseña', [
        validators.Required(),
        validators.Length(min=7,message='La contraseña debe tener 7 caracteres como mínimo'),
        validators.EqualTo('confirm', message='La contraseña debe coincidir con la repetición')
    ])
    confirm = PasswordField('Repite la contraseña')
    accept_tos = BooleanField('Acepto las condiciones', [validators.Required()])

@app.route("/", methods=['GET', 'POST'])
def inicio():
     global __count__
     save_hist(request)
     return render_template("inicio.html", sesiones=html_sessions())

@app.route('/formulario', methods=['GET', 'POST'])
def register():
    global __count__
    save_hist(request)
    form = Formulario2(request.form)
    db_datos={}
    if request.method == 'POST' and form.validate():
        db[form.username.data]=form.password.data
        #Guardamos los datos en la otra BD
        guardar_datos(form)
        session['username'] = form.username.data  #Lo almacenamos en las sesiones
        return redirect('/')
    return render_template("formulario.html", form=form, sesiones=html_sessions())

@app.route('/login', methods=['GET', 'POST'])
def login():
    global __count__
    save_hist(request)
    form=Login(request.form)
    user=form.username.data
    if 'username' in session: #Si hay una sesion activa
        Logeado=True
        return render_template("login.html",form=form,Logeado=Logeado, sesiones=html_sessions())
    elif request.method == 'POST' and form.validate() and user in db: #Si está registrado
        session['username'] = form.username.data #Lo almacenamos en las sesiones
        return redirect('/')
    elif request.method == 'POST' and user not in db:
        return redirect('/formulario') #Redireccionamos al formulario de registro
    else:
        Logeado=False
        return render_template("login.html",form=form,Logeado=Logeado, sesiones=html_sessions())

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    save_hist(request)
    session.pop('username', None)
    return redirect('/')

@app.route('/visualizar')
def visualizar():
     global __count__
     save_hist(request)
     if 'username' in session:
        user=session['username']
        '''
        Vamos a crear un diccionario para almacenar los datos y poder pasarlo como parametro
        '''
        dic=db_datos[str(user)]
        return render_template("visualizar.html",dic=dic,username=user,sesiones=html_sessions())
     else:
        return redirect('/')


if __name__ == "__main__":
    app.debug=True
    app.run()
