# Import the Pandas library
import pandas as pd


from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import json
import requests
from pandas.io.json import json_normalize

import os
import numpy as np


app = Flask(__name__)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run()