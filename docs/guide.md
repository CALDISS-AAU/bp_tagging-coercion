# Prodigy guide - tagging coercion



This guide describes how to work with prodigy on a strato instance.



[TOC]

## 1. Setup strato instance

- Setup standard ubuntu instance on strato
- Associate floating IP
- Open ports for prodigy interface - preferably several to have multiple instances running (fx 8070, 8080, 8090)



## 2. Setup prodigy

- Install prodigy on instance using provided wheel

- Prodigy should preferably be installed in its own virtual environment (https://docs.python.org/3/tutorial/venv.html)

  - ```bash
    # example
    
    python3 -m virtualenv prodigy # ubuntu 20
    source prodigy/bin/activate
    ```



## 3. Prepare data

- Prepare data in accordance with the valid input formats: https://prodi.gy/docs/api-loaders
- NOTE: Prodigy expects the text to be tagged to be stored in the key "text" (all lower-case)



## 4. Prepare bash script for prodigy instance

- Prepare a bash script for starting prodigy instance using the appropriate recipe: https://prodi.gy/docs/recipes

- The script should include the following:

  - Activating the prodigy environment
  - Creating relevant environment variables (fx port, authorization): https://prodi.gy/docs/install#env-variables
  - Line for launching the instance (using nohup)

**Example 1 (ner tagging instance): `prodigy_tagging.sh`**

```bash
#!/bin/bash

source prodigy/bin/activate

export PRODIGY_PORT="8090" # Make sure the port used is opened
export PRODIGY_BASIC_AUTH_USER="user"
export PRODIGY_BASIC_AUTH_PASS="passwd"
export PRODIGY_ALLOWED_SESSIONS="names,seperated,by,commas"

nohup prodigy ner.manual tagged_dataname_out blank:da path/to/inputdata --label LABEL1,LABEL2 &> nohup.out &
```



**Example 2 (review instance): `prodigy_review.sh`**

```bash
#!/bin/bash

source prodigy/bin/activate

export PRODIGY_PORT="8090" # Make sure the port used is opened
export PRODIGY_BASIC_AUTH_USER="user"
export PRODIGY_BASIC_AUTH_PASS="passwd"
export PRODIGY_ALLOWED_SESSIONS="names,seperated,by,commas"

nohup prodigy review reviewed_dataname_out tagged_dataname_in --label LABEL1,LABEL2 &> nohup.out &
```



  ## 5. Configure Prodigy

- Create a "prodigy.json" file to configure prodigy: https://prodi.gy/docs/install#config
- Make sure to specify host to match the internal IP of the strato instance (not the floating IP)
- If multiple taggers are used to tag the same entries, make sure to enable "feed_overlap"



**Example `prodigy.json`**

```
{
	"host": "10.0.100.200",	# internal IP for strato instance
	"feed_overlap": true 	# enables feed_overlap - taggers tagging the same entries
}
```



## 6. Launch prodigy instance

- Launch the instance by running the relevant file, fx: `bash prodigy_tagging.sh`
- You can validate the instance is running by checking `htop`
- Inspect the nohup.out file for possible errors if not launched
- When launced the instance can be accessed using the floating IP and the port
- Remember that if the environment variable `PRODIGY_ALLOWED_SESSIONS`, the url has to include `/?session=validname`



## 7. Close prodigy instance

- Close the instance by sending a "sigint" signal to the running process
  - Open `htop`
  - Find the process for the prodigy instance (there will be several with identical names so find the longest running one)
  - Hit F9 ("Kill")
  - Choose option 2 ("SIGINT")



## 8. (optional) Merge with existing data

- If the tagged data is to be merged with other data, use the db-recipes to merge the data: https://prodi.gy/docs/recipes#db-merge

- Example: `prodigy db-merge inputset1,inputset2 outputname`
- Make sure the prodigy environment is activate (`source prodigy/bin/activate`)



**Merge datasets with same texts**

- If the data to be merged are identical sets with different tags, adopt the code below

https://support.prodi.gy/t/merging-annotations-from-different-datasets/310/2

```{python}
from prodigy.components.db import connect
from prodigy.models.ner import merge_spans
from prodigy import set_hashes

db = connect()
datasets = ['tc_anno-ents_reviewed', 'tc_anno-names_reviewed']
examples = []

for dataset in datasets:
     examples += db.get_dataset(dataset)

merged = merge_spans(examples)
merged_data = [set_hashes(eg, overwrite = True) for eg in merged]
db.add_dataset('tc_names-ents-merged')
```



## 9. (optional) Export tagged data

- The tagged data can be exported using `db-out`: https://prodi.gy/docs/recipes#db-out



## 10. Train the model

- Train the model using the appropriate recipe: https://prodi.gy/docs/recipes#training

- Models can be trained from a blank model or using an existing model:

  - From blank model (danish): `prodigy train ner tagged_data blank:da`
  - From existing model (danish) : `prodigy train ner tagged_data da_core_news_lg`
    - NOTE: This requires that the language model (from spacy) is already installed: https://spacy.io/models
  - Note the default settings for train/test split (`--eval-split`)



**Evaluate how accuracy improves with data**

- The recipe `train-curve` can be used to evaluate whether the model would benefit from more data: https://prodi.gy/docs/recipes#train-curve
- From blank model (danish): `prodigy train-curve ner tagged_data blank:da --n-samples 10`
- From existing model (danish) : `prodigy train-curve ner tagged_data da_core_news_lg --n-samples 10`



**Saving and using the model**

- The model can be stored using the `--output` option in the `train` recipe to specify an output directory for the trained model
- The model can then be loaded like any other spacy model: https://spacy.io/api/top-level#spacy.load 

