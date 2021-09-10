import argparse
import json
import os
from azureml.core import Run, Model
from shutil import copy2

parser = argparse.ArgumentParser()
parser.add_argument('--saved-model', type=str, dest='saved_model', help='path to saved model file')
args = parser.parse_args()

print("registering model:", args.saved_model)

model_output_dir = './outputs/'

os.makedirs(model_output_dir, exist_ok=True)
out_file = copy2(args.saved_model, model_output_dir)


run = Run.get_context()


run.upload_file(out_file, out_file)
model = run.register_model( model_name='hr-analytics-ds-prediction',
                             model_path=out_file)