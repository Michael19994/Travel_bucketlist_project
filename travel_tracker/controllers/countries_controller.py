from flask import Flask, render_template
from flask import Blueprint
from models.countries import Country
import repositories.countries_repository as countries_repository


countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries", methods=["GET"])
def countries():
    countries = countries_repository.select_all()
    return render_template("countries/index.html", countries=countries)

@countries_blueprint.route("/countries/<id>")
def showing_countries(id):
    countries_shown = countries_repository.select(id)
    return render_template("countries/show.html", country=countries_shown)

@countries_blueprint.route("/countries/new")
def add_country():
    every_country = countries_repository.select_all()
    return render_template("/countries/new.html", countries=every_country)

