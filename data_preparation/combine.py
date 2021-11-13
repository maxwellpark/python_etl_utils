import glob
import pandas as pd 

path = './data_files/'
files = glob.glob(path + '*.csv')

frames = []

for file in files: 
    # Frame per file
    df = pd.read_csv(file, index_col=None, sep=',', header=0)
    print(df)
    frames.append(df)

# Combine frames 
frame = pd.concat(frames, axis=0, ignore_index=True)

# Write to 1 CSV
frame.to_csv(path + "combined_data.csv")
