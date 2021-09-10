from azureml.core.run import Run
import pandas as pd
import argparse

run = Run.get_context()
ws = run.experiment.workspace



def main():


    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_prefix", type=str,required=True)
    parser.add_argument("--register_datasets", type=str, nargs="*",required=True)
    args = parser.parse_args()



    print(args.register_datasets)
    for key in args.register_datasets:
        print(key)

        dataset = run.input_datasets[key]
        dataset_name = "{}_{}".format(args.dataset_prefix,key)
        description = "{}_{} registered in pipeline step"

        dataset.register(ws,name=dataset_name, description=description,create_new_version=True)



if __name__=="__main__":
    main()