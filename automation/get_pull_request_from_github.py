import requests
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
json_response = response.json()


# for one entry
print(json_response[0]['user']['login'])

for  i in range(len(json_response)):
    print(json_response[i]['user']['login'])
