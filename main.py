import requests
response = requests.get("https://owlbot.info/api/v4/dictionary/dog",headers={'Authorization':'Token 9baac545bdccb5ff98dcdb55ecec1613987d4150'})
print(response.status_code)
print(response.json())