import requests

api_key = "BuStGJZLeBHtW9OBnRUK"
latitude = "49.187706"
longitude = "-122.850060"
radius = "500"
headers = {"Accept": "application/xml"}
url = f"http://api.translink.ca/RTTIAPI/V1/stops?apiKey={api_key}&lat={latitude}&long={longitude}&radius={radius}"

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.text
    print(data)
else:
    print("Error:", response.status_code)