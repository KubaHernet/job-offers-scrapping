import requests

base_url = "https://justjoin.it/api"
get_offers_endpoint = f"{base_url}/base/v2/user-panel/offers/by-cursor"
get_offer_details_endpoint = f"{base_url}/justjoinit/job-advertisements/"

params = {
    "orderBy": "DESC",
    "sortBy": "salary",
    "categories[]": [5, 25],
    "itemsCount": 10,
    "remoteWorkOptions[]": "remote"
}

def get_offers():
    response = requests.get(get_offers_endpoint, params=params)

    print(f"Requested URL: {response.url}")


    if response.status_code == 200:
        data = response.json()
        offers = data.get("data", [])
        return offers
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return []
    
def get_offer_details(offer_id):
    url = f"{get_offer_details_endpoint}{offer_id}"
    response = requests.get(url)

    print(f"Requested URL: {response.url}")

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve offer details for ID {offer_id}: {response.status_code}")
        return None