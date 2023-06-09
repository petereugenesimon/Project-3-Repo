import numpy as np
import sqlite3
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

from flask import Flask, jsonify, render_template


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/deathSTATSKEY.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
COD = Base.classes.deathStats

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def main_page():
    
    return render_template('index.html')

@app.route("/api/v1.0/cods")
def cods():
    # Connect to the SQLite database
    session = Session(engine)

    # Query all rows from the table
    results = session.query(COD).all()

    # Define an empty list to store the JSON objects
    cods_list = []

    # Iterate over the results and convert each row to a dictionary
    for row in results:
        cods_dict = {
            "id": row.id,
            "year": row.year,
            "state": row.state,
            "all_causes": row.all_causes,
            "natural_cause": row.natural_cause,
            "septicemia": row.septicemia,
            "malignant_neoplasms": row.malignant_neoplasms,
            "diabetes": row.diabetes,
            "alzheimers": row.alzheimers,
            "influenza_pneumonia": row.influenza_pneumonia,
            "lower_respiratory": row.lower_respiratory,
            "other_respiratory": row.other_respiratory,
            "nephritis": row.nephritis,
            "abnormal": row.abnormal,
            "heart_disease": row.heart_disease,
            "cerebrovascular_diseases": row.cerebrovascular_diseases,
            "covid": row.covid
        }
        cods_list.append(cods_dict)

    # Close the session
    session.close()

    # Return the JSON response
    return jsonify(cods_list)

if __name__ == '__main__':
    app.run(debug=False)