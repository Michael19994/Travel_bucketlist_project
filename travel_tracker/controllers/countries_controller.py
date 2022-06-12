from flask import Flask, render_template
from flask import Blueprint
from models.countries import Country
import repositories.countries_repository as countries_repository


countries_blueprint = Blueprint("name", __name__)