import json
import numpy as np
import os
import joblib
import glob
import pandas as pd
from numpy import nan

from sklearn.base import TransformerMixin
from utils import StringCaster
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType
from inference_schema.schema_decorators import input_schema, output_schema


input_sample = pd.DataFrame(data=[{"city": "city_103",
 "city_development_index": 0.92,
 "gender": "Male",
 "relevent_experience": "No relevent experience",
 "enrolled_university": "no_enrollment",
 "education_level": "High School",
 "major_discipline": nan,
 "experience": "6",
 "company_size": nan,
 "company_type": nan,
 "last_new_job": "never",
 "training_hours": 66},
 {"city": "city_21",
 "city_development_index": 0.624,
 "gender": "Male",
 "relevent_experience": "Has relevent experience",
 "enrolled_university": "no_enrollment",
 "education_level": "Masters",
 "major_discipline": "STEM",
 "experience": "11",
 "company_size": "50-99",
 "company_type": "Early Stage Startup",
 "last_new_job": ">4",
 "training_hours": 46}])
 
def init():        

    global model

    print("modeldir",os.getenv("AZUREML_MODEL_DIR") )


    filename = os.getenv("AZUREML_MODEL_DIR")+"/model.pkl"

    with open(filename, "rb") as fil: 
        model = joblib.load(fil)
    

@input_schema('data', PandasParameterType(input_sample, enforce_shape=False))
def run(data):
    # print(request)
    # data = json.loads(request)
    # data = pd.DataFrame(data.get("data"))
    

    try:
        result = model.predict(data)
        return json.dumps({"result": result.tolist()})
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
