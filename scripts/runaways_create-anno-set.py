import json
import random
import os

# Set directories and filenames
datadir = os.path.join("D:/", "data", "runaways")
filename = "runaways_annotate.json" # To read in
outname = "runaways_annotate-names_01.json" # To export

datapath = os.path.join(datadir, filename)
outpath = os.path.join(datadir, outname)

# Load data
with open(datapath, 'r', encoding = 'utf-8') as f:
    data = json.load(f)
    f.close()


# Creating random sample of 200 integers    
random.seed(402)
sample_integers = random.sample(range(len(data)), 200)   


# Creating sample of 200 entries based on integers
data_sample = []

for i in sample_integers:
    data_sample.append(data[i])
    
    
# Export sample data
with open(outpath, 'w', encoding = 'utf-8') as f:
    json.dump(data_sample, f, ensure_ascii=False)

