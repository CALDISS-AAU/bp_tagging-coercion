# Snippets



**Merge datasets with same texts**

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

