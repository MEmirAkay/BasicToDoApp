from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/admin/Desktop/ToDoApp/todo.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html",todos=todos)

@app.route("/complete/<string:id>")
def completeTask(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/add",methods = ["POST"])
def addTodo():
    title = request.form.get("title")
    detail = request.form.get("detail")
    newTodo = Todo(title = title, detail = detail, complete = False)

    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    detail = db.Column(db.String(80))
    complete = db.Column(db.Boolean)




if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
