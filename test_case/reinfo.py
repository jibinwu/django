import json
import requests
url='http://114.55.43.36:7091/api/getReInfo'
headers={'authorization':'Bearer def34b98-7276-48b1-b857-fc5dae045214','Content-Type':'application/json'}
content={'plateNo':'浙F9992X','cityCode':9}
r=requests.post(url,headers=headers,data=json.dumps(content))
print(r.text)
print(r.url)
print(r.encoding)
print(r.content)
