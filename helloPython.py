import requests

response = requests.get("https://www.saramin.co.kr/zf_user/")

html = response.text

print(html)