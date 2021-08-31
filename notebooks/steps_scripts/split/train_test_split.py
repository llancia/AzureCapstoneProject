from azureml.core import Run

import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
import argparse

def stratified_split(df, label="target"):
    X = df.drop(columns=[label])
    y = df[label]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state = 99)

    train = pd.concat((X_train,y_train), axis=1)
    test =  pd.concat((X_test,y_test), axis=1)

    return train,test

    
parser = argparse.ArgumentParser()
parser.add_argument('--train_path', dest='train_output_path', required=True)
parser.add_argument('--test_path', dest='test_output_path', required=True)


args = parser.parse_args()
    
ds = Run.get_context().input_datasets['prepped_data']
df = ds.to_pandas_dataframe()

df_train, df_test = stratified_split(df)


os.makedirs(args.train_output_path, exist_ok=True) 
os.makedirs(args.test_output_path, exist_ok=True) 

df_train.to_csv(os.path.join(args.train_output_path, "train.csv"), index=False)
df_test.to_csv(os.path.join(args.test_output_path, "test.csv"), index=False)


