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

@app.route("/api/v1.0/cods")
def cods():
  
    session = Session(engine)

    # Query all passengers
    results = session.query(COD.Year).all()

    session.close()

    cods_list = []
    for Year, State in results:
        cods_dict = {}
        cods_dict["Year"] = Year
        cods_list.append(cods_dict)

    return jsonify(cods_list)

if __name__ == '__main__':
    app.run(debug=False)