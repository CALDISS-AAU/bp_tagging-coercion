import os
import json

with open("../data/Runaway_ads.json", 'r', encoding = 'utf8') as f:
    data = json.load(f)

error_ids = ['E-0694', 'E-3022']
	
docs = [doc for doc in data if doc['ID'] not in error_ids] 

for doc in docs:
	doc['text'] = doc.pop('Text')
	
data_out = os.path.join("..", "data", "runaways_annotate.json")

with open(data_out, 'w', encoding = 'utf8') as f:
	json.dump(docs, f, ensure_ascii=False)