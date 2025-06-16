import requests
url = 'https://www.linkedin.com/in/chethan-kumar-profile/'
response = requests.get(url)
print(response.text)
