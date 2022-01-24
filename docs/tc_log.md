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



#### 2022-01-19

- Saved elasticsearch settings files in elasticzip.zip in project folder on OneDrive
- 
