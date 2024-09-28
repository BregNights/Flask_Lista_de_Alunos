
from flask import Flask, render_template, request
from classes import StudentControl

def base_context():
    students_db = StudentControl()

    return {
        "msg": "Lista de Alunos Apex",
        "student_list": students_db.get_students(),
    }

app = Flask(__name__)

@app.route('/')
def index():

    context = base_context()

    return render_template('index.html', context=context)

@app.route('/add', methods=['POST'])
def add_new_student():

    students_db = StudentControl()

    new_student = {
        "name": request.form['name'],
        "email": request.form['email'],
        "course": request.form['course']
    }

    students_db.create_student(**new_student)
    context =  base_context()

    return render_template('lista.html', context=context)

@app.route('/list')
def lista_students():

    context =  base_context()

    return render_template('lista.html', context=context)

@app.route('/delete', methods=['POST', 'GET'])
def delete_students():

    students_db = StudentControl()
    students_db.delete_student(id=request.args.get("id"))

    context =  base_context()

    return render_template('lista.html', context=context)

@app.route('/update', methods=['POST', 'GET'])
def update_students():

    students_db = StudentControl()
    students_db.update_student(id=request.args.get("id"))

    context =  base_context()

    return render_template('update.html', context=context)

app.run()