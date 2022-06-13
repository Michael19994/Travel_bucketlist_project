from flask import Flask, redirect, render_template, request
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

@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    country = request.form['country']
    region = request.form['region']
    new_country = Country(country, region)
    countries_repository.save(new_country)
    return redirect("/countries")

@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = countries_repository.select(id)
    return render_template("/countries/edit.html", country=country)  
    

@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form['name']
    region = request.form['region']
    edited_country = Country(name, region, id)
    countries_repository.update(edited_country)
    return redirect("/countries")

@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_country(id):
    countries_repository.delete(id)
    return redirect("/countries")
