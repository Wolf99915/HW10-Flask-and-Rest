from app import app, db
from flask import render_template, request, redirect
from models.models import Plant

@app.route("/add-plant")
def add_plant():
    return render_template("add_plant.html")

@app.route("/save-plant", methods=["POST"])
def save_plant():
    name = request.form.get("name")
    location = request.form.get("location")
    plant = Plant(title=name, location=location)
    db.session.add(plant)
    db.session.commit()
    return redirect("/")

@app.route("/delete-plant/<int:id>")
def delete_plant(id):
    plant = Plant.query.get(id)
    db.session.delete(plant)
    db.session.commit()
    return redirect("/")

@app.route("/plants")
def plants():
    return render_template("plants.html")

@app.route("/about-plant/<int:id>")
def about_plant(id):
    # plant = Plant.query.get(id)
    # print(plant)
    # return render_template("/about_plant.html", plant=plant)
    plant = Plant.query.get(id)
    # employees = Employee.query.filter(Employee.plant_id == id)
    return render_template("about_plant.html", plant=plant)



