from azureml.core import Dataset, Datastore
from azureml.core import Workspace
import os

ws = Workspace.from_config()

def main():
    datastore =  ws.get_default_datastore()

    dataset_name = "HrAnalytics-DataScientist"
    description = """ """
    local_path = r"../data/"
    dataset_file = 'aug_train.csv'
    datastore_path = 'udacity-lancia'
    datastore.upload(src_dir=local_path, target_path=datastore_path)


    dataset_file_remote = os.path.join(datastore_path,dataset_file)
    ds = Dataset.Tabular.from_delimited_files(path=[(datastore, (dataset_file_remote))])
    ds = ds.register(ws,
                    name= dataset_name,
                    description=description)
    
if __name__ == "__main__":
    main()
