from requests import get as g
import bs4
import json
import os

res = g('https://api.github.com/users/Amritansh-Ashesh')
json_data = json.loads(res.text)
os.system(f'start \"\" {json_data["blog"]}')