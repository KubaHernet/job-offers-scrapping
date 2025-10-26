import requests
import json
import just_join_it.just_join_it_client as just_join_it_client
from utils.collection_utils import remove_duplicates

offers = just_join_it_client.get_offers()

if len(offers) > 0:
    offers = remove_duplicates(offers, lambda x: x.get("guid"))

    with open("offers/just_join_it/offers.json", "w") as file:
        json.dump(offers, file, indent=4)

    print("Data saved to offers.json")

    top_ten_offers = offers[:10]
    for offer in top_ten_offers:
        offer_id = offer.get("guid")
        details = just_join_it_client.get_offer_details(offer_id)
        if details:
            with open(f"offers/just_join_it/items/{offer.get("slug")}.json", "w") as file:
                json.dump(details, file, indent=4)
else:
    print("Failed to retrieve data or no offers found.")