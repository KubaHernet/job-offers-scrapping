import requests

base_url = "https://justjoin.it/api/base/v2/user-panel/offers/by-cursor"

params = {
    "orderBy": "DESC",
    "sortBy": "salary",
    "categories[]": [5, 25],
    "itemsCount": 5,
    "remoteWorkOptions[]": "remote"
}

def get_offers():
    response = requests.get(base_url, params=params)

    print(f"Requested URL: {response.url}")


    if response.status_code == 200:
        data = response.json()
        offers = data.get("data", [])
        return offers
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return []