import sys
import os
import json
import requests
import config as cfg

#URL
analysis_id = requests.post(cfg.base_url, headers = {"x-apikey": cfg.my_key}, data = {"url": cfg.query_url}).json()
print (analysis_id)
#URL{ID}
only_id = (analysis_id.get('data').get('id'))[2:]
#URL{ID}/ANALYSE
build_url = cfg.base_url + "/" + only_id + "/analyse"
happening = requests.post(cfg.base_url, headers = {"x-apikey": cfg.my_key}, data = {"url": build_url})
print(happening.text)
#ANALYSES/ID