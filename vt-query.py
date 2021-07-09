import sys
import os
import json
import requests
import config as cfg


print (cfg.post_url)
result = requests.post(cfg.post_url, headers = {"x-apikey": cfg.my_key}, data = {"url": cfg.query_url})
print(result.text)
