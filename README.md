<p align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Udacity_logo.png/800px-Udacity_logo.png" alt="Logo">
  </a>
  <h1 align="center">Azure Machine Learning Engineer | Capstone Project</h1>
    <p align="center">
    project_description
    <br/>
</p>

A company is sponsorizing some courses for data scientist and wanto to hire potential candidates.

Many people signup for their training. Company wants to know which of these candidates are really wants to work for the company after training.

Information related to demographics, education, experience are in hands from candidates signup and enrollment.


## Project Set Up and Installation
From the raw data available [here](https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists) i've set up a pipeline that prepare the data for either the hyperparmaeter search and for automl task.

It also take care of train and test splitting.

Details are available in the notebook `notebooks/create_dataset.ipynb`


## Dataset
The original dataset contains:
- enrollee_id : Unique ID for candidate
- city: City code
- city_ development _index : Developement index of the city (scaled)
- gender: Gender of candidate
- relevent_experience: Relevant experience of candidate
- enrolled_university: Type of University course enrolled if any
- education_level: Education level of candidate
- major_discipline :Education major discipline of candidate
- experience: Candidate total experience in years
- company_size: No of employees in current employer's company
- company_type : Type of current employer
- lastnewjob: Difference in years between previous job and current job
- training_hours: training hours completed
- target: 0 – Not looking for job change, 1 – Looking for a job change


Note:

- The dataset is imbalanced.
- Most features are categorical (Nominal, Ordinal, Binary), some with high - cardinality.
- Missing imputation can be a part of your pipeline as well.
 about the data you are using and where you got it from.

### Task
We have to predict which data scientist is looking for a job change and thus, is a better prospect in terms of hiring.

### Access

By running the SetUp Pipeline, from the original dataset we register two different datasets

![img\1.png]()

- `HRAnalytics_train_dataset`
- `HRAnalytics_test_dataset`

![img\2.png]()

we can then access using the following python code: 

```{python}
# Dataset
dataset_name = "HRAnalytics_train_dataset"

dataset = ws.datasets[dataset_name]

df = dataset.to_pandas_dataframe()
df.head()
```


## Automated ML

In this first step, an AutoML run was lunched to search for a best possible model to handle the predictive task.

An `AutoMLConfig` is the the object we need to instantiate to configuring the experiment run:

```{python}

automl_settings = {
    "experiment_timeout_minutes": 20,
    "max_concurrent_iterations": 4,
    "n_cross_validations": 4,
    "primary_metric" : 'AUC_weighted'
}

automl_config = AutoMLConfig(compute_target=compute_cluster,
                             task="classification",
                             label_column_name="target",   
                             training_data =dataset,
                             enable_early_stopping=True,
                             featurization='auto',
                             debug_log="automl_errors.log",
                             **automl_settings
                            )
```

The parameters are:

- **experiment_timeout_minutes**: maximum amount of time in minutes that all iterations combined can take before the experiment terminates. It has been set to 20

- **max_concurrent_iterations**: maximum number of iterations that would be executed in parallel. It has been set to 4

- **n_cross_validations**: how many cross validations to perform when user validation data is not specified. It has been set to 4

- **primary_metric**: the metric that Automated Machine Learning will optimize for model selection. It has been set to AUC weighted between classes


### Results
After submitting the run to the Compute cluster we wait for it to complete by monitoring the widget: 

![img/3.png]()

After it's done we can get the result of the AutoML job by gathering the:

* best run
* the best model
* the metrics associate to the best model
using the following code
```

best_run_automl, best_model_automl = remote_run.get_output()
best_run_metrics_automl = best_run_automl.get_metrics()

```

We fetched the model and tested it against the `test_dataset` we held for the purpose:

```
y_true = test_df["target"]
x = test_df.drop(columns=["target"])

y_pred= best_model_automl.predict(x)
```

The best model is a Voting Ensamble achieving a AUC weighted of 0.80
```
PipelineWithYTransformations(Pipeline={'memory': None,
                                       'steps': [('datatransformer',
                                                  DataTransformer(enable_dnn=False, enable_feature_sweeping=True, feature_sweeping_config={}, feature_sweeping_timeout=86400, featurization_config=None, force_text_dnn=False, is_cross_validation=True, is_onnx_compatible=False, observer=None, task='classification', working_dir='/mn...
)), ('extratreesclassifier', ExtraTreesClassifier(bootstrap=False, ccp_alpha=0.0, class_weight='balanced', criterion='gini', max_depth=None, max_features=None, max_leaf_nodes=None, max_samples=None, min_impurity_decrease=0.0, min_impurity_split=None, min_samples_leaf=0.01, min_samples_split=0.056842105263157895, min_weight_fraction_leaf=0.0, n_estimators=200, n_jobs=1, oob_score=False, random_state=None, verbose=0, warm_start=False))], verbose=False))], flatten_transform=None, weights=[0.06666666666666667, 0.3333333333333333, 0.06666666666666667, 0.13333333333333333, 0.06666666666666667, 0.13333333333333333, 0.13333333333333333, 0.06666666666666667]))],
                                       'verbose': False},
                             y_transformer={},
                             y_transformer_name='LabelEncoder')
                             
```


## Hyperparameter Tuning

In this task, an HyperDrive run  using a customized model is built.

The model chosen is a RandomForest with its scikit-learn implementation.

RandomForest is a classification algorithm using a bagging of different trees. It has a very good resistance to overfitting and quite a lot of different hyperparameters to tune.

To ensure the different data are ready to be handeled by the classifier an sklearn pipeline is built around it as staded in the `train.py` script.


```
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

```

The script can be lunched by passing different parameters representig some of  the hyperparameters of the model: 

```
    parser.add_argument('--n_estimators', type=int )
    parser.add_argument('--max_features', type=str)
    parser.add_argument('--max_depth', type=int)
```

* **n_estimator** is the number of the tree composing the ensamble
* **max_features** is the rule 
* **max_depth**

We went through the combination of parameters to search the best one via a Random search which it does not give the absolute best parameters but its usually pretty close and helps in reducing the iteratons w.r.t a Grid Search approach.

To do this we defiend a parameter space

```
```
and a early termination policy


to finally submit a Hyperdrive run


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
