import requests

user_url: str = input("Type url: ")

headers = { 
  "apikey": "ef0a64c0-67af-11ed-9a00-55621cc4b54e"}

params = (
   ("url", user_url),
   ("premium","true"),
   ("country","us"),
   ("render","true"),
);


response = requests.get('https://app.zenscrape.com/api/v1/get', headers=headers, params=params);

print(response.text)

required: list[str] = []
for i in range(len(response.text)):
    required_course: str = response.text[i:i+15]
    if required_course[0:11] == "Total Hours":
        break
    if required_course[0:7] == "this, '":
        if not required_course[7:15] in required:
            required.append(required_course[7:15])
print(required)