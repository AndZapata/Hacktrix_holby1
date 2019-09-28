#!/usr/bin/python3
""" flask app to integrate data to provide charts to html"""
from flask import Flask, render_template, url_for

app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

@app.route('/chart')
def smart_chart():
    """ handles the info to the chart
    """
    data = {
        "chapinero": 50,
        "chapinero2": 32,
        "usaquen": 15
    }

    return render_template('index.html', data=data)

if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(debug=True, host=host, port=port)
