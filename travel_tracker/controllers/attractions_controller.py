from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.attractions import Attraction
import repositories.attractions_repository as attractions_repository
import repositories.destinations_repository as destinations_repository
from models.destinations import Destination


attractions_blueprint = Blueprint("attractions", __name__)

@attractions_blueprint.route("/attractions", methods=["GET"])
def attractions():
    attractions = attractions_repository.select_all()
    return render_template("attractions/index.html", attractions=attractions)

@attractions_blueprint.route("/attractions/<id>")
def showing_attractions(id):
    attractions_shown = attractions_repository.select(id)
    return render_template("attractions/show.html", attraction=attractions_shown)

@attractions_blueprint.route("/attractions/new")
def add_attraction():
    every_destination = destinations_repository.select_all()
    return render_template("/attractions/new.html", destinations=every_destination)

@attractions_blueprint.route("/attractions/new", methods=["POST"])
def create_attraction():
    name = request.form['name']
    description = request.form['description']
    destination = request.form['destination']
    date = request.form['date']
    visited = request.form['visited']
    new_destination = Destination.select(destination)
    new_attraction = Attraction(name, description, new_destination, date, visited)
    attractions_repository.save(new_attraction)
    return redirect("/attractions")

@attractions_blueprint.route("/attractions/<id>edit")
def edit_attraction(id):
    attraction = attractions_repository.select(id)
    every_destination = destinations_repository.select_all()
    return render_template("/attractions/edit.html", attraction=attraction, destination=every_destination)

@attractions_blueprint.route("/attractions", methods=["POST"])
def update_attraction():
    name = request.form['name']
    description = request.form['description']
    destination = request.form['destination']
    date = request.form['date']
    visited = request.form['visited']
    new_destination = destinations_repository.select(destination)
    edited_attraction = Attraction(name, description, new_destination, date, visited)
    attractions_repository.update(edited_attraction)
    return redirect("/attractions")

@attractions_blueprint.route("/attractions<id>/delete", methods=["POST"])
def delete_attraction(id):
    attractions_repository.delete(id)
    return redirect("/attractions")



