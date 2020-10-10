# privacy_deidentification

notion link
https://www.notion.so/71894069da3b4bbba7c6f6c9854ec8f9

    /privacy
    |
    ├── ./dataset                       //Datasets
    │   ├── dataset.csv     
    │   ├── temp_data.csv
    │   ├── monthly_income.csv
    |
    ├── ./result                        //De-identification Result
    |
    ├── ./temp_code                     
    |   ├── input_v1.py                 //csv input program - one by one
    |   ├── input_v2.py                 //csv input program - every csv files on the path
    |   ├── input_v3.py                 //csv input program - one by one using pandas
    |   ├── output_v1.py                //csv output program - extract python list to csv file
    |   ├── output_v2.py                //csv input program - extract pandas dataframe to csv file
    |
    ├── generalization.py               //codes for generalization
    ├── statistical_processing.py       //codes for statistical-processing
    ├── randomized.py                   //codes for randomized-processing
    ├── main.py                         //codes for input and output csv
    |
