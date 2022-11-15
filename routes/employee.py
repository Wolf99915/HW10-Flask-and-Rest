from app import app, db
from flask import render_template, request, redirect
from models.models import Employee

@app.route("/add-plant")
def add_plant():
    return render_template("add_employee.html")

@app.route("/save-employee", methods=["POST"])
def save_plant():
    name = request.form.get("name")
    object_id = request.form.get("object_id")
    type_of_work = request.form.get("type_of_work")
    employee = Employee(name=name, object_id=object_id, type_of_work=type_of_work)
    db.session.add(employee)
    db.session.commit()
    return redirect("/")

@app.route("/delete-employee/<int:id>")
def delete_plant(id):
    employee = Employee.query.get(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect("/")

@app.route("/employees")
def plants():
    return render_template("employee.html")

@app.route("/about-employee/<int:id>")
def about_plant(id):
    employees = Employee.query.get(id)
    print(employees)
    return render_template("/about_employee.html", plant=plant)
