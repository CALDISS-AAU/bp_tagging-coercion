# Log for Tagging Coercion



#### 2021-07-02

- All data stored in "tc_data_20210720.zip" (strato instance + workstation)

- Latest datasets:

  - "tc_anno-place": All places tagged as "place" (by JH)
  - "tc_anno-ents_comb": Names, addresses and cities tagged - several rounds and reviewed (by JH and ADB)

- Last training run:

  - `prodigy train-vurve ner tc_anno-ents_comb da_core_news_lg --n-samples 10 --eval-split 0.2`

    - 74.13% accuracy
    - +2.39 difference from 90% to 100% data - could benefit from more tagging

  - `prodigy train-vurve ner tc_anno-place da_core_news_lg --n-samples 10 --eval-split 0.2`

    - 80.65% accuracy
    - -0.18 difference from 90% to 100% data - possibly no benefit from additional tagging

    

#### 2021-11-15

- Started tagging of nouns ("fællesnavne") i tc_ner-set2.json using bash file `prodigy_annotate_nouns_pos.sh`
- Using `pos.correct`: https://prodi.gy/docs/recipes#pos 
- Using spacy model [da_core_news_lg](https://spacy.io/models/da#da_core_news_lg): https://spacy.io/models/da#da_core_news_lg
- Stored to dataset `tc_pos_nouns` 



#### 2021-11-24

- Trying to isolate problematic tags

- In terms of training a model, it makes no difference whether the dataset contains several labels (tagged spans) or the labels are spread across different datasets (with the same texts and tokens)

  - Added three datasets: `tc_ADDRESS_20210702.json`, `tc_CITY_20210702.json`, `tc_NAME_20210702.json` - split from `tc_anno-ents_comb_20210702.jsonl` using `data-handling.ipynb`
  - Model performance seems to worsen if a model is trained on single tags

- Best model precision achieved by *not* starting with existing spacy model

- Result for: `prodigy train ner tc_anno-ents_comb da_core_news_lg --eval-split 0.2`

  ![image-20211124163831736](./img/image-20211124163831736.png)

- Result for: `prodigy train ner tc_anno-ents_comb blank:da --eval-split 0.2`

  ![image-20211124164027029](./img/image-20211124164027029.png)


#### 2022-01-19

- Saved elasticsearch settings files in elasticzip.zip in project folder on OneDrive



#### 2022-01-24

- Exporting data from old-strato to zip "tc-export_20220124" and moving to new instance on new strato
- Original data order in database:
  - test_test
    test_runaways
    runaways_anno-guide
    runaways_anno-names
    tc_anno-verbs
    runaways_anno-names_reviewed
    tc_anno-verbs_reviewed
    tc_anno-ents
    tc_anno-ents_reviewed
    tc_anno-names_reviewed
    tc_names-ents_reviewed
    tc_names-ents-merged
    tc_anno-place
    tc_anno-ents2
    tc_anno-ents2_reviewed
    tc_anno-ents_comb
    tc_pos-nouns
    tc_ADDRESS_20210702
    tc_CITY_20210702
    tc_NAME_20210702



#### 2022-01-24

- Exploring combination-options between data tagged via NER and POS recipes - overall same structure
- POS recipe splits sentences by default - "unsegmented" option. May make sense to re-do POS-tagging with manually split sentences.



#### 2022-02-09

- Creating dataset containing all text pieces used for annotation: `tc_annotate-set-all-mixed_20220902.json`
  - Used "data_handling.ipynb"

