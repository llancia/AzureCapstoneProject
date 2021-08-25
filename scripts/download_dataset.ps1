mkdir -p data
cd data 
kaggle datasets download --force -d arashnic/hr-analytics-job-change-of-data-scientists
unzip -o *.zip
rm *.zip
cd ..
