import requests

param={
  "q":"python",
  "sort":"stars",
  "order":"desc",
  "per_page":5
}

response=requests.get("https://api.github.com/search/repositories", params=param)
data=response.json()
items=data["items"]

for i in items:
  print(i["full_name"])
  print(i["stargazers_count"])