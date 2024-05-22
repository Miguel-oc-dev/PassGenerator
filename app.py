from flask import Flask, render_template, request
import random
import string

app=Flask(__name__)

#Generador de contraseñas
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

#Seccion para las rutaS
@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        password = generate_password(length)
    #return "<h1>PassGenerator</h2>"
    return render_template('index.html', password=password)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)