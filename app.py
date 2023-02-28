from flask import Flask, request, render_template, redirect, make_response, flash
from flask_wtf import CSRFProtect

import forms
from Programa import Calculadora, Traductor

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
#csrf = CSRFProtect(app)

@app.route('/')
def mainn():
    return redirect('/cajas_dinamica')

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    registrar_Alumno = forms.UserForm(request.form)
    Mat = ''
    Nom = ''
        
    if request.method == 'POST' and registrar_Alumno.validate():
        Mat = registrar_Alumno.matricula.data
        Nom = registrar_Alumno.nombre.data
    
    return render_template('alumnos.html', form = registrar_Alumno, mat=Mat, nom = Nom, name="Alumnos")

@app.route('/cajas_dinamica', methods=['GET', 'POST'])
def method_name(): 
    Active = False
    Ns = 0
    
    if request.method == 'POST':
        Ns = int(request.form.get('numero'))
        Active = Ns != 0
    
    return render_template('cajas.html', active = Active, ns = Ns, name="Cajas Dinámicas")


@app.route('/calcular', methods=['GET', 'POST'])
def calcular():
    Numeros = Calculadora.get_Array(request.form)
    
    return render_template("calcular.html",
                           numeros = Numeros,
                           repetidos = Calculadora.contar_repeticiones(Numeros),
                           comas = Calculadora.concatenar_Numeros(Numeros),
                           promedio = Calculadora.promedio(Numeros),
                           nMenor = Calculadora.num_Menor(Numeros),
                           nMayor = Calculadora.num_Mayor(Numeros),
                           name = "Resultado de " + str(len(Numeros)) + " números")

@app.route('/cookie', methods=['GET', 'POST'])
def cookies():
#    return 'HOLA'
    reg_user = forms.LoginForm(request.form)
    response = make_response(render_template('cookie.html', name = 'Cookie', form = reg_user))
    
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        passw = reg_user.password.data
        datos = user + '@' + passw
        success_message = 'Bienvenido {}'.format(user)
        response.set_cookie('datos_user', datos)
        flash(success_message)
    
    return response

@app.route('/traductor', methods=['GET', 'POST'])
def traductor():
    reg_palabra = forms.Languages(request.form)
    result = ''
    word = ''
    
    if request.method == 'POST':
        status = request.form.get('status')
        if status == 'registrar' and reg_palabra.validate():
            span = reg_palabra.spanish.data
            en = reg_palabra.english.data
            Traductor.guardar(span, en)
        elif status == 'buscar':
            word = request.form.get('word')
            lan = request.form.get('select')
            result = "Resultado: {}".format(Traductor.buscar_Palabra(word, lan))
            
    
    return render_template('traductor.html', name='Traductor', form=reg_palabra, result = result, search = word)

if __name__ == "__main__":
    #csrf.init_app(app)
    app.run(debug = True, port=3000)
