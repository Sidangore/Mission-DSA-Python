import requests
username = "siddhantangore"
base_url = "https://leetcode.com/u/" + username
r = requests.post(base_url)
print(r.text)


