from flask import Flask, redirect, render_template, request
from flask import Blueprint
from models.destinations import Destination
import repositories.destinations_repository as destination_repository


destinations_blueprint = Blueprint("destinations", __name__)

@destinations_blueprint.route("/destinations", methods=["GET"])
def destinations():
    destinations = destination_repository.select_all()
    return render_template("destinations/index.html", destinations=destinations)

@destinations_blueprint.route("/destinations/<id>")
def showing_destinations(id):
    destinations_shown = destination_repository.select(id)
    return render_template("destinations/show.html", destination=destinations_shown)


