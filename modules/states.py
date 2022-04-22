from imports import requests

url = "https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_hash.json"
r = requests.get(url)
states = r.json()

'''Remove expanded name and replace with 0'''
for key, val in states.items():
    states[key] = 0