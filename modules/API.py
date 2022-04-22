from imports import requests

# Connect to API
url = "https://data.cdc.gov/resource/n8mc-b4w4.json"
r = requests.get(url)
content = r.json()
print(len(content))
