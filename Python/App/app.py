from flask import Flask ,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)


class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    dsce=db.Column(db.String(500),nullable=False)
    Date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno}-{self.title}"


@app.route("/" ,methods=["GET","POST"])
def home():
    if request.method=="POST":
        title=(request.form["title"])
        dsce=(request.form["dsce"])
        todo=Todo(title=title,dsce=dsce)
        db.session.add(todo)
        db.session.commit()
    allTodo=Todo.query.all()
    return render_template("index.html",allTodo=allTodo)


@app.route("/Update")
def Update():
    allTodo=Todo.query.all()
    print(allTodo)
    return "<h1>This is my Product Page</h1>"

@app.route("/delete/<int:sno>")
def delete(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect("/")

@app.route("/todos")
def show_todos():
    todos = Todo.query.all()
    return "<br>".join([f"{t.sno}: {t.title} - {t.dsce}" for t in todos])

@app.route("/About", methods=["POST","GET"])
def About():


    return render_template("About.html")

if  __name__=="__main__" :
    with app.app_context():
        db.create_all()

    app.run(debug=True)