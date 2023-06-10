from flask import render_template, request, redirect, url_for
from app import app
from app.models import Todo
from app import db
from datetime import datetime

@app.route('/')
def index():

    #incomplete = Todo.query.filter_by(complete=False).all()
    #complete = Todo.query.filter_by(complete=True).all()
    Items=Todo.query.all()
    for i in Items:
        date_created=(str(i.date_created).split(" "))
        i.date_created=date_created[0]

    return render_template('index.html',Items=Items)


@app.route('/add', methods=['POST'])
def add():
    d=datetime.strptime(request.form['todo_date'],'%Y-%m-%d')

    print(d)
    print(request.form['Options'])
    todo = Todo(text=request.form['todoitem'], complete="Incomplete",
                priority=request.form['Options'], date_created=d)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = "Complete"
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/remove/<id>')
def remove(id):
    print(id)
    todo = Todo.query.filter_by(id=int(id)).first()
    db.session.delete(todo)
    db.session.commit()
    return  redirect(url_for('index'))

@app.route('/update/<id>', methods=['GET','POST'])
def update(id):
    todo = Todo.query.filter_by(id=id).first()
    if request.method=="POST":

        todo.text=request.form['todoitem']
        todo.date_created=datetime.strptime(request.form['todo_date'],'%Y-%m-%d')
        todo.priority = request.form['Options']
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', todo=todo)

