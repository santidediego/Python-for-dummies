from flask import Flask
from flask import render_template,request,session, redirect, url_for,escape,Response
#from flask.ext import shelve
#Este modulo es una extension de shelve, shelve ya viene por defecto aunque podemos usar esta también
from wtforms import Form, BooleanField, TextField, PasswordField, TextAreaField, SelectField, RadioField, DateField, validators
#Regexp es para validar expresiones regulares

import dbm
app = Flask(__name__)
__count__=0
__first_time__=True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#Las dos siguientes sentencias sirven para que funcione shelve. Solo necesario si trabajamos con la extension
#app.config['SHELVE_FILENAME'] = 'shelve.db'
#shelve.init_app(app)

db = dbm.open('base_datos.dat', 'c')
db_datos = dbm.open('datos_usuarios','c') #Esta la usaremos para almacenar datos de usuarios

"""
Historial
"""

def deleteFirst(lista):
    for j in range(2):
        lista[str(j)]=lista[str(j+1)]
def save_hist(request):
    global __count__
    global __first_time__
    if __count__ == 2:
        if __first_time__:
            __first_time__=False
        else:
            deleteFirst(session)
        session[str(__count__)]=str(request.url)
    else:
        session[str(__count__)]=str(request.url)
        __count__+=1

def html_sessions():
    global __count__
    ses_html=list()
    for j in range(0,__count__):
        print (j)
        ses_html.append(session[str(j)])
    return ses_html

def invalidPassword(form,field):
    if form.username.data in db:
        if not db[form.username.data] == bytes(field.data,'utf-8') :
            raise validators.ValidationError('Contraseña incorrecta')


def guardar_datos(form):
        db_datos['Usuario: ']=str(form.username.data)
        db_datos['DNI: ']=str(form.DNI.data)
        db_datos['Fecha de nacimiento: ']=str(form.date.data)
        db_datos['Email: ']=str(form.email.data)
        db_datos['Dirección: ']=str(form.adress.data)
        db_datos['Método de pago: ']=str(form.payment.data)
        db_datos['VISA: ']=str(form.VISA.data)
        db_datos['Contraseña: ']=str(form.password.data)

class Login(Form):
    username = TextField('Nombre de Usuario', [validators.Length(min=4, max=25)])
    password = PasswordField('Contraseña', [
        validators.Required(),
        invalidPassword
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
        db_datos={} #Reinicializamos datos
        return redirect('/')
    elif request.method == 'POST' and user not in db:
        return redirect('/formulario') #Redireccionamos al formulario de registro
    else:
        Logeado=False
        return render_template("login.html",form=form,Logeado=Logeado, sesiones=html_sessions())

@app.route('/logout')
def logout():
    save_hist(request)
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect('/')

@app.route('/visualizar')
def visualizar():
    global __count__
    save_hist(request)
    if 'username' in session and db_datos!={}:
        user=session['username']
        '''
        Vamos a crear un diccionario para almacenar los datos y poder pasarlo como parametro
        '''
        dic={}
        #El método decode convierte bytes en str y el método encode convierte str en bytes
        dic['Usuario: ']=db_datos['Usuario: '].decode('utf-8')
        dic['DNI: ']=db_datos['DNI: '].decode('utf-8')
        dic['Fecha de nacimiento: ']=db_datos['Fecha de nacimiento: '].decode('utf-8')
        dic['Email: ']=db_datos['Email: '].decode('utf-8')
        dic['Dirección: ']=db_datos['Dirección: '].decode('utf-8')
        dic['Método de pago: ']=db_datos['Método de pago: '].decode('utf-8')
        dic['VISA: ']=db_datos['VISA: '].decode('utf-8')
        dic['Contraseña: ']=db_datos['Contraseña: '].decode('utf-8')

        return render_template("visualizar.html",dic=dic, sesiones=html_sessions())
    else:
        return redirect('/')


if __name__ == "__main__":
    app.debug=True
    app.run()
