#!/usr/bin/env python
# coding: utf-8

# In[41]:


import os
import json

# Paths
data_path = os.path.join("D:/", "data", "tagging-coercion")
filename1 = "Tekst_til_tagging_juni2021.json"
filename2 = "runaways_annotate-names_01.json"
outname = "tc_ner-set.json"

# Read data
with open(os.path.join(data_path, filename1), 'r', encoding = "utf-8") as f:
    data1 = json.load(f)
    
with open(os.path.join(data_path, filename2), 'r', encoding = "utf-8") as f:
    data2 = json.load(f)

# Rename text key
for entry in data1:
    entry['text'] = entry['Text']
    entry['set'] = entry['Datasæt']
    entry.pop('Text', None)
    entry.pop('Datasæt', None)

# Add set key
for entry in data2:
    entry['set'] = 'runaways'
    
# Combine
data = data1 + data2

# Write
with open(os.path.join(data_path, outname), 'w', encoding = 'utf-8') as f:
    json.dump(data, f)

