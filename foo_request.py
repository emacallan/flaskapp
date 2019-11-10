import requests
url = 'http://localhost:8080/amount'
payload = "{\n\t\"account_id\": \"4d468e92-413f-4cca-8115-abb18c264d15\",\n\t\"amount\" : 7\n}"
headers = {
  'Content-Type': 'application/json',
  'Transaction-Id': '7943f961-a733-43cf-ba3d-905a5856f6da'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False, )
print(response.text)


url = 'http://localhost:8080/balance/4d468e92-413f-4cca-8115-abb18c264d15'
payload = {}
headers = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False,)
print(response.text)