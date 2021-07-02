#!/usr/bin/env python
# coding: utf-8

import os
import json

# Paths
data_path = os.path.join("D:/", "data", "tagging-coercion")
filename = "Tekst_til_tagging_juni2021.json"
outname = "tc_ner-set2.json"

# Read data
with open(os.path.join(data_path, filename), 'r', encoding = "utf-8") as f:
    data = json.load(f)

# Rename text key
for entry in data:
    entry['text'] = entry['Text']
    entry['set'] = entry['Datasæt']
    entry.pop('Text', None)
    entry.pop('Datasæt', None)

# Write
with open(os.path.join(data_path, outname), 'w', encoding = 'utf-8') as f:
    json.dump(data, f)

