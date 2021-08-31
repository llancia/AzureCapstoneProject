import argparse
from utils import StringCaster
import os
from typing import Tuple

import joblib
import numpy as np
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from sklearn.compose import ColumnTransformer
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.base import TransformerMixin
from sklearn.metrics import accuracy_score, roc_auc_score, matthews_corrcoef
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import FunctionTransformer


    

def create_pipeline(**classifier_params):
    numeric_features = ['city_development_index', 'training_hours']

    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())])

    categorical_features = ['city',  'gender', 'relevent_experience',
        'enrolled_university', 'education_level', 'major_discipline',
        'experience', 'company_size', 'company_type', 'last_new_job']

    categorical_transformer = Pipeline(steps=[
        ('caster', StringCaster()),
        ('encoder', OneHotEncoder(handle_unknown='ignore')),
        ]
    )


    preprocessor = ColumnTransformer(
        transformers=[ 
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])


    clf = Pipeline(steps=[('preprocessor', preprocessor),
                        ('classifier', RandomForestClassifier(**classifier_params))])


    return clf

run = Run.get_context()


def stratified_split(df, label="target"):
    X = df.drop(columns=[label])
    y = df[label]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state = 99)


    return X_train,X_test , y_train, y_test

def get_data() -> pd.DataFrame:
    data = run.input_datasets['train_data']
    return data.to_pandas_dataframe()


def log_metrics(x_test,y_test,model):
   
    y_pred_score = model.predict_proba(x_test)[:,-1]
    y_pred = model.predict(x_test)
    
    accuracy = accuracy_score( y_test,y_pred)
    run.log("Accuracy", np.float(accuracy))
    
    auc = roc_auc_score(y_test, y_pred_score)
    run.log("AUC", np.float(auc))



def dump_model(model,model_out_path="./outputs/model", m_file_name="/model.joblib"):
    os.makedirs(model_out_path, exist_ok=True)
    joblib.dump(model, model_out_path+m_file_name)


def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--n_estimators', type=int )
    parser.add_argument('--max_features', type=str)
    parser.add_argument('--max_depth', type=int)


    
    args = parser.parse_args()

    run.log("No Estimators:", np.int(args.n_estimators))
    run.log("Max Features:", args.max_features)
    run.log("Max Depth:", np.int(args.max_depth))

    x_train, x_test, y_train, y_test = stratified_split(get_data())


    model = create_pipeline(n_estimators=args.n_estimators,
    max_features=args.max_features,
    max_depth=args.max_depth)
    model.fit(x_train, y_train)

    log_metrics(x_test,y_test,model)
    dump_model(model)




if __name__ == '__main__':
    main()
