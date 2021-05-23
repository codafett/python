from random import randint
import requests

url = "https://icanhazdadjoke.com/search"

topic = input("Enter a topic: ")

response = requests.get(
    url, headers={"Accept": "application/json"}, params={"term": topic}
)

if response.ok:
    data = response.json()
    min = max(data["total_jokes"], data["limit"])
    num = randint(0, min - 1)
    print(f"Found {data['total_jokes']} on the topic of {topic}, here's one:")
    print(data["results"][num]["joke"])

else:
    print("Failed to get jokes")
