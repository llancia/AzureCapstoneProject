import argparse
import json
import os
from azureml.core import Run, Model
from shutil import copy2
import joblib
from utils import StringCaster

run = Run.get_context()

def get_data() -> pd.DataFrame:
    data = run.input_datasets['test_data']
    return data.to_pandas_dataframe()

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--saved-model', type=str, dest='saved_model', help='path to saved model file')


    args = parser.parse_args()

    print("registering model:", args.saved_model)

    model_output_dir = './outputs/'

    os.makedirs(model_output_dir, exist_ok=True)
    out_file = copy2(args.saved_model, model_output_dir)



    with open(out_file, "rb") as f:  
        model = joblib.load(f)

    model.predict(get_data())


if __name__ == '__main__':
    main()
