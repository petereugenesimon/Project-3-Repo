import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

from flask import Flask, jsonify, render_template


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/cod.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
COD = Base.classes

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

@app.route("/api/v1.0/cod")
def cod():
  
    session = Session(engine)

    # Query all passengers
    results = session.query(COD.Year, COD.State, COD.NaturalCause,
                            COD.Diabetes, COD.Alzheimerdisease, COD.Influenza_pneumonia,
                            COD.Symptomsnotelsewhereclassified, COD.Diseasesofheart,
                            COD.COVID_19MultipleCauseofDeath, COD.COVID_19UnderlyingCauseofDeath).all()

    session.close()

    # cod_list = []
    # for Year, State, NaturalCause, Diabetes, Alzheimerdisease, Influenza_pneumonia, Symptomsnotelsewhereclassified, Diseasesofheart, COVID_19MultipleCauseofDeath, COVID_19UnderlyingCauseofDeath in results:
    #     cod_dict = {}

    # return jsonify(results)

if __name__ == '__main__':
    app.run(debug=False)