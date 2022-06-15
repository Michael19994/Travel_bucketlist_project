from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.destinations import Destination
import repositories.destinations_repository as destination_repository
import repositories.countries_repository as countries_repository
from models.countries import Country

destinations_blueprint = Blueprint("destinations", __name__)

@destinations_blueprint.route("/destinations", methods=["GET"])
def destinations():
    destinations = destination_repository.select_all()
    return render_template("destinations/index.html", destinations=destinations)

@destinations_blueprint.route("/destinations/<id>")
def showing_destinations(id):
    destinations_shown = destination_repository.select(id)
    return render_template("destinations/show.html", destination=destinations_shown)

@destinations_blueprint.route("/destinations/new")
def add_destination():
    every_country = countries_repository.select_all()
    return render_template("/destinations/new.html", countries=every_country)

@destinations_blueprint.route("/destinations", methods=["POST"])
def create_destination():
    name = request.form['name']
    country = request.form['country']
    new_country = countries_repository.select(country)
    new_destination = Destination(name, new_country)
    destination_repository.save(new_destination)
    return redirect("/destinations")

@destinations_blueprint.route("/destinations/<id>/edit")
def edit_destination(id):
    destination = destination_repository.select(id)
    every_country = countries_repository.select_all()
    return render_template("/destinations/edit.html", destination=destination, countries=every_country)

@destinations_blueprint.route("/destinations/<id>", methods=["POST"])
def update_destination(id):
    name = request.form['name']
    country = request.form['country']
    new_country = countries_repository.select(country)
    edited_destination = Destination(name, new_country, id)
    destination_repository.update(edited_destination)
    return redirect("/destinations")

@destinations_blueprint.route("/destinations/<id>/delete", methods=["POST"])
def delete_destination(id):
    destination_repository.delete(id)
    return redirect("/destinations")


