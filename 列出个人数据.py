import requests
import json

url = "https://api.gologin.com/browser/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NGI1MjkzNDBjNGE0OWQ4NmRkNWZjYTciLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NGI1MmM4Mzc0ZjUyNDc3YTJkZGY5ZjgifQ.AqUkAwhhEuSTryypsG_i7PChKaBghWyL2oOnilQCwoU"

payload = {}
headers = {
  'Authorization': f'Bearer {token}',
  'Content-Type': 'application/json'
}
response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text)

profiles = data["profiles"]
ids = []

for profile in profiles:
    print(f"Name: {profile['name']}    ID: {profile['id']}")
    ids.append(profile['id'])

# Use the IDs in your main code as needed
for profile_id in ids:
    # Perform operations with each profile ID
    print(f"Using profile ID: {profile_id}")
    # Your code here
