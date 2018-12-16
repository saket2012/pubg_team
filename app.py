from flask import render_template, Flask
from flask import request

from manager import ramdon_forest_duo, ramdon_forest_squad

app = Flask(__name__)
wsgi_app = app.wsgi_app


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/homepage")
def homepage():
    return render_template('homepage.html')


@app.route('/prediction_squad')
def prediction_squad():
    return render_template('prediction_squad.html')


@app.route('/prediction_squad_output', methods = ['POST'])
def prediction_squad_output():
    f = request.files['file']
    placement = ramdon_forest_squad(f)
    return render_template('prediction_squad_output.html', placement = placement)

@app.route('/prediction_duo')
def prediction_duo():
    return render_template('prediction_duo.html')


@app.route('/prediction_duo_output', methods = ['POST'])
def prediction_duo_output():
    f = request.files['file']
    placement = ramdon_forest_duo(f)
    return render_template('prediction_duo_output.html', placement = placement)


if __name__ == "__main__":
    app.run(debug = True)
