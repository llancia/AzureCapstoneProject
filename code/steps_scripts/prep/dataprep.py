from azureml.core import Run

import pandas as pd 
import numpy as np 
import argparse

def make_target(df):

    df.target = df.target.map({1.0: "yes", 0.0: "no"})

    return df

def drop_cols(df) -> pd.DataFrame:

    return df.drop(columns=["enrollee_id"])

    
parser = argparse.ArgumentParser()
parser.add_argument('--output_path', dest='output_path', required=True)
args = parser.parse_args()
    
ds = Run.get_context().input_datasets['input_ds']
df = ds.to_pandas_dataframe()

df = make_target(df)
df = drop_cols(df)

os.makedirs(args.output_path, exist_ok=True) 
df.to_csv(os.path.join(args.output_path, "prepped.csv"), index=False)

print(f"Wrote prepped data to {args.output_path}/prepped_data.csv")
