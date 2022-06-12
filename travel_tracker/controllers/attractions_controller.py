from flask import Flask, render_template
from flask import Blueprint
from models.attractions import Attraction
import repositories.attractions_repository as attractions_repository
import repositories.countries_repository as countries_repository
import repositories.destinations_repository as destination_repository

attractions_blueprint = Blueprint("name", __name__)