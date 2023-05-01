import pandas as pd
from glob import glob
## import csv file from src/data/raw

single_file_src = pd.read_csv("../../data/raw/MetaMotion/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Accelerometer_12.500Hz_1.4.4.csv")
single_file_gyr = pd.read_csv("../../data/raw/MetaMotion/MetaMotion/A-bench-heavy_MetaWear_2019-01-14T14.22.49.165_C42732BE255C_Gyroscope_25.000Hz_1.4.4.csv")
## import all csv files from src/data/raw
files =glob("../../data/raw/MetaMotion/MetaMotion/*.csv")
len(files)

f=files[0]

# remove the file path from the file name
file = f.split('/')[-1].split('\\')[-1]

