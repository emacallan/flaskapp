import requests
url = 'http://localhost:8080/amount'
payload = "{\n\t\"account_id\": \"a40bcc03-6f39-418c-ad0b-97e14f522ec1\",\n\t\"amount\" : 7\n}"
headers = {
  'Content-Type': 'application/json',
  'Transaction-Id': '7943f961-a733-43cf-ba3d-905a5856f6da'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)
print(payload,headers)
input()

url = 'http://localhost:8080/balance/a40bcc03-6f39-418c-ad0b-97e14f522ec1'
payload = {}
headers = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False,)
print(response.text)
print(payload,headers)
input()

url = 'http://localhost:8080/balance/a40bcc03-6f39-418c-ad0b-97e14f522ec1'
payload = {}
headers = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)
print(payload,headers)
input()


url = 'http://localhost:8080/amount'
payload = "{\n\t\"account_id\": \"a40bcc03-6f39-418c-ad0b-97e14f522ec1\",\n\t\"amount\" : 13\n}"
headers = {
  'Content-Type': 'application/json',
  'Transaction-Id': '3bc387f1-f46e-45b1-9ab7-4f6840181f19'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

print(payload,headers)
input()

url = 'http://localhost:8080/balance/a40bcc03-6f39-418c-ad0b-97e14f522ec1'
payload = {}
headers = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

print(payload,headers)
input()

url = 'http://localhost:8080/amount'
payload = "{\n\t\"account_id\": \"a40bcc03-6f39-418c-ad0b-97e14f522ec1\",\n\t\"amount\" : -10\n}"
headers = {
  'Content-Type': 'application/json',
  'Transaction-Id': '1f80bf52-5f0b-41d7-95f9-6e61a1734298'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

print(payload,headers)
input()

url = 'http://localhost:8080/balance/a40bcc03-6f39-418c-ad0b-97e14f522ec1'
payload = {}
headers = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

print(payload,headers)
input()

url = 'http://localhost:8080/amount'
payload = "{\n\t\"account_id\": \"a40bcc03-6f39-418c-ad0b-97e14f522ec1\",\n\t\"amount\" : 10\n}"
headers = {
  'Content-Type': 'application/json'
}
response = requests.request('PUT', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

print(payload,headers)
input()

url = 'http://localhost:8080/amount'
payload = "{\n\t\"account_id\": \"a40bcc03-6f39-418c-ad0b-97e14f522ec1\",\n\t\"amount\" : 13\n}"
headers = {
  'Content-Type': 'application/xml',
  'Transaction-Id': '59b2917e-6407-40eb-8fbf-287435fcd6f8'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

print(payload,headers)
input()

url = 'http://localhost:8080/amount'
payload = "{\n\t\"amount\" : 13\n}"
headers = {
  'Content-Type': 'application/json',
  'Transaction-Id': '6eadf15c-fc8a-4584-b708-31a56df13563'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

print(payload,headers)  
input()

url = 'http://localhost:8080/amount'
payload = "{\n\t\"account_id\": \"a40bcc03-6f39-418c-ad0b-97e14f522ec1\"\n}"
headers = {
  'Content-Type': 'application/json',
  'Transaction-Id': '6eadf15c-fc8a-4584-b708-31a56df13563'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

input()

url = 'http://localhost:8080/amount'
payload = "{\n\t\"account_id\": \"a40bcc03-6f39-418c-ad0b-97e14f522ec1\",\n\t\"amount\" : \"dafadf\"\n}"
headers = {
  'Content-Type': 'application/json',
  'Transaction-Id': 'da0b5092-8f41-4774-87be-16cc3a778549'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

input()

url = 'http://localhost:8080/amount'
payload = "{\n\t\"account_id\": 5,\n\t\"amount\" : 10\n}"
headers = {
  'Content-Type': 'application/json',
  'Transaction-Id': 'da439f4b-c969-4445-b296-1dd4cc93477e'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

input()

url = 'http://localhost:8080/balance/4a53a8f5-036c-4851-a86a-401abd01e1a7'
payload = {}
headers = {}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

input()

url = 'http://localhost:8080/amount'
payload = "{\n\t\"account_id\": \"855b825b-d684-41ec-8320-145520591126\",\n\t\"amount\" : 7\n}"
headers = {
  'Content-Type': 'application/json',
  'Transaction-Id': 'd23bd187-a8ca-464b-87d7-120a89553644'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

input()

url = 'http://localhost:8080/amount'
payload = "{\n\t\"account_id\": \"855b825b-d684-41ec-8320-145520591126\",\n\t\"amount\" : 7\n}"
headers = {
  'Content-Type': 'application/json',
  'Transaction-Id': 'd23bd187-a8ca-464b-87d7-120a89553644'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)


