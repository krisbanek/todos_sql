from flask import Flask, request, render_template, redirect, url_for
from forms import ToDoForm
from models_sql import todos

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/todos/", methods=["GET", "POST"])
def todos_list():
    form = ToDoForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            data_dict = form.data
            data_list = (data_dict["zadanie"], data_dict["opis"], data_dict["status"])
            todos.create(data_list)
        return redirect(url_for("todos_list"))
             
    return render_template("todos.html", form=form, todos = todos.all(), error=error)

@app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
def todos_details(todo_id):
    todo = todos.get_by_id(todo_id)
    form = ToDoForm(data = todo)
    
    if request.method == "POST":
        if form.validate_on_submit():
            data_dict1 = form.data
            z = data_dict1["zadanie"]
            o = data_dict1["opis"]
            s = data_dict1["status"]
            todos.update(todo_id, zadanie=z, opis=o, status=s)
        return redirect(url_for("todos_list"))   
    return render_template("todo_id.html", form=form, todo_id=todo_id)

if __name__ == "__main__":
    app.run(debug=True)