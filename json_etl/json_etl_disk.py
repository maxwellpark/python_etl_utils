import pandas as pd
import json

j_dict = dict()

with open("./data.json") as f: 
    # Convert JSON to dictionary
    j_dict = json.load(f)

# Create dataframe 
df0 = pd.DataFrame.from_dict(j_dict[0], orient="index")
print(df0)


