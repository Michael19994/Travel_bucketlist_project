from flask import Flask, render_template

from controllers.attractions_controller import attractions_blueprint
from controllers.countries_controller import countries_blueprint
from controllers.destinations_controller import destinations_blueprint

app = Flask(__name__)

app.register_blueprint(attractions_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(destinations_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

