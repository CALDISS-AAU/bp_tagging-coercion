import json
import random
import os
import re

# Set directories and filenames
datadir_out = os.path.join("D:/", "data", "tagging-coercion")
datadir_runaways = os.path.join("D:/", "data", "runaways")
datadir_interrogations = os.path.join("D:/", "data", "interrogations")
filename_runaways = "runaways_annotate.json" 
filename_interrogations = "Interrogation_raw.json" 
outname = "tagging-coercion_annotate-verbs_01.json" # To export

datapath_runaways = os.path.join(datadir_runaways, filename_runaways)
datapath_interrogations = os.path.join(datadir_interrogations, filename_interrogations)
outpath = os.path.join(datadir_out, outname)

# Load data
with open(datapath_runaways, 'r', encoding = 'utf-8') as f:
    data_runaways = json.load(f)
    f.close()

for doc in data_runaways:
    doc['set'] = "runaways"

with open(datapath_interrogations, 'r', encoding = 'utf-8') as f:
    data_interrogations = json.load(f)
    f.close()

for doc in data_interrogations:
    doc['text'] = doc.pop('Text')
    doc['set'] = "interrogations"

regex = r'(?<=[a-zA-Z])\.(?=\s[A-Z])'

data_interrogations_split = []

for doc in data_interrogations:
    split_text = re.split(regex, doc.get('text'))
    chunk_count = 1
    for chunk in split_text:
        entry_dict = {}
        entry_dict['ID'] = doc.get('ID')
        entry_dict['Date'] = doc.get('Date')
        entry_dict['Reference'] = doc.get('Reference')
        entry_dict['Name'] = doc.get('Name')
        entry_dict['text'] = chunk
        entry_dict['chunk'] = chunk_count
        entry_dict['set'] = doc.get('set')
        
        data_interrogations_split.append(entry_dict)
        
        chunk_count = chunk_count + 1

# Creating random sample of 2x150 integers    
random.seed(202)
sample_integers_runaways = random.sample(range(len(data_runaways)), 150)   
sample_integers_interrogations = random.sample(range(len(data_interrogations_split)), 150)   

# Creating sample of 300 entries based on integers
data_sample = []

for i in sample_integers_runaways:
    data_sample.append(data_runaways[i])

for i in sample_integers_interrogations:
    data_sample.append(data_interrogations_split[i])
    
# Shuffle data
random.shuffle(data_sample)

# Export sample data
with open(outpath, 'w', encoding = 'utf-8') as f:
    json.dump(data_sample, f, ensure_ascii=False)

