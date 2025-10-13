import requests
import json

base_url = "https://justjoin.it/api/base/v2/user-panel/offers/by-cursor"

params = {
    "orderBy": "DESC",
    "sortBy": "salary",
    "categories[]": [5, 25],
    "itemsCount": 5,
    "remoteWorkOptions[]": "remote"
}

def remove_duplicates(items, selector):
    seen = set()
    unique_items = []
    for item in items:
        key = selector(item)
        if key and key not in seen:
            unique_items.append(item)
            seen.add(key)
    return unique_items

response = requests.get(base_url, params=params)

print(f"Requested URL: {response.url}")


if response.status_code == 200:
    data = response.json()
    offers = data.get("data", [])
    unique_offers =   remove_duplicates(offers, lambda x: x.get("guid"))

    with open("offers.json", "w") as file:
        json.dump(unique_offers, file, indent=4)

    print("Data saved to offers.json")
else:
    print(f"Failed to retrieve data: {response.status_code}")
