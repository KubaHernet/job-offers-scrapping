import requests
import json
import just_join_it.just_join_it_client as just_join_it_client
from utils.collection_utils import remove_duplicates

offers = just_join_it_client.get_offers()

if len(offers) > 0:
    unique_offers =   remove_duplicates(offers, lambda x: x.get("guid"))

    with open("offers.json", "w") as file:
        json.dump(unique_offers, file, indent=4)

    print("Data saved to offers.json")
else:
    print("Failed to retrieve data or no offers found.")
