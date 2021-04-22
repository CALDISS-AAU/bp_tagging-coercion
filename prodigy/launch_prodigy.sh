source prodigy/bin/activate # activate virtual environment
export PRODIGY_BASIC_AUTH_USER="username" # set username
export PRODIGY_BASIC_AUTH_PASS="password" # set password
prodigy ner.manual test_runaways blank:da ./data/runaways_annotate.json --label PERSON # start prodigy