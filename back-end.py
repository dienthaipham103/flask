import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
df = pd.read_csv('global.csv')
countries = df.to_dict('record')

df1 = pd.read_csv('table.csv')
information = df1.to_dict('record')

df2 = pd.read_csv('most_cases.csv')
most_cases = df2.to_dict('record')

df3 = pd.read_csv('case_pie.csv')
most_cases_pie = df3.to_dict('record')


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
            <p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/countries/all', methods=['GET'])
def api_all():
    return jsonify(countries)

@app.route('/information/all', methods=['GET'])
def api_all1():
    return jsonify(information)

@app.route('/most_cases/all', methods=['GET'])
def api_all2():
    return jsonify(most_cases)

@app.route('/most_cases_pie/all', methods=['GET'])
def api_all3():
    return jsonify(most_cases_pie)


@app.route('/countries', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for country in countries:
        if country['id'] == id:
            results.append(country)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)




app.run()