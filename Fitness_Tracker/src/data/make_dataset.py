import pandas as pd

from glob import glob

## import csv file from src/data/raw

single_file_src = pd.read_csv(
    "../../data/raw/MetaMotion/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Accelerometer_12.500Hz_1.4.4.csv"
)
single_file_gyr = pd.read_csv(
    "../../data/raw/MetaMotion/MetaMotion/A-bench-heavy_MetaWear_2019-01-14T14.22.49.165_C42732BE255C_Gyroscope_25.000Hz_1.4.4.csv"
)
## import all csv files from src/data/raw
files = glob("../../data/raw/MetaMotion/MetaMotion/*.csv")
len(files)

f = files[0]

# remove the file path from the file name
file = f.split("/")[-1].split("\\")[-1]
# split the file name using the '-' delimiter into its components

parts = file.split("-")
# print(parts)
# assign the first part to the participant variable
participant = parts[0]
# print(participant)
subparts = parts[1].split("_")
# print(subparts)
# use slicing to extract the label and category from the second subpart
label = subparts[0]
# print(label)
subparts = parts[2].split("_")
print(subparts)
category = subparts[0][:-1]
# print(category)
# print the resulting variables
# print(participant, label, category)

## create a dataframe to store data extracted from file as features in dataframe

df = pd.read_csv(f)
df["participant"] = participant
df["label"] = label
df["category"] = category
df
##create 2 dataframes for accelerometer and gyroscope files to process filename and store features
acc_df = pd.DataFrame()
gyro_df = pd.DataFrame()
##create an identifier to set
acc_set = 1
gyro_set = 1
##loop through all files in the list and store them to dataframes
for f in files:
    

    file = f.split("/")[-1].split("\\")[-1]
    parts = file.split("-")
    participant = parts[0]
    subparts = parts[1].split("_")
    label = subparts[0]
    subparts = parts[2].split("_")
    category = subparts[0][:-1]
    df = pd.read_csv(f)
    df["participant"] = participant
    df["label"] = label
    df["category"] = category
    if "Accelerometer" in f:
        df['set'] = acc_set
        acc_set += 1
        acc_df = pd.concat([acc_df, df])
        acc_df
    elif "Gyroscope" in f:
        df['set'] = gyro_set
        gyro_set += 1
        gyro_df = pd.concat([gyro_df, df])
        gyro_df
        
        gyro_df[gyro_df['category'] == 'heavy']