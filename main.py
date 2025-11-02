import json
import os
import just_join_it.just_join_it_client as just_join_it_client
from utils.collection_utils import remove_duplicates
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv




def get_offer_required_skills(offer_description_html: str):
    text = BeautifulSoup(offer_description_html, "html.parser").get_text()
    prompt = f"""
    Extract 3–5 key technical skills, tools, or technologies mentioned in this job description.
    Return them as a JSON list.

    Job description: {text}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
            details_html = details.get("body")
            required_skills = get_offer_required_skills(details_html)
            print(f"extracted skills for {offer_id}: {required_skills}")
else:
    print("Failed to retrieve data or no offers found.")
