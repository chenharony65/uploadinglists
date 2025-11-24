"""
Simple internal tool for managing my Etsy shop listings.

- Reads product data from a local CSV file that I fill in manually.
- Creates DRAFT listings based on that data.
- Updates existing listings (title, price, tags, etc.) in bulk.

This tool is only used by me for my own shop.
"""

import csv
import os
import time
import requests
from typing import Dict, Any


class EtsyClient:
    """
    Minimal Etsy API client for my internal use.
    """

    def __init__(self, api_key: str, shop_id: str, access_token: str):
        self.api_key = api_key
        self.shop_id = shop_id
        self.access_token = access_token
        self.base_url = "https://openapi.etsy.com/v3/application"

    def _headers(self) -> Dict[str, str]:
        return {
            "x-api-key": self.api_key,
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def create_draft_listing(self, product: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new DRAFT listing from manually prepared product data.
        """
        payload = {
            "title": product["title"],
            "description": product["description"],
            "who_made": "i_did",
            "when_made": "made_to_order",
            "is_supply": False,
            "taxonomy_id": int(product["taxonomy_id"]),
            "price": product["price"],                  # string
            "quantity": int(product["quantity"]),
            "tags": product["tags"].split("|"),
            "materials": product["materials"].split("|"),
            "state": "draft",                           # keep as draft
        }

        url = f"{self.base_url}/shops/{self.shop_id}/listings"
        response = requests.post(url, headers=self._headers(), json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        print(f"Created draft listing: {data.get('listing_id')}")
        return data

    def update_listing(self, listing_id: str, product: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an existing listing (title, price, tags, etc.).
        """
        payload = {
            "title": product["title"],
            "description": product["description"],
            "price": product["price"],
            "quantity": int(product["quantity"]),
            "tags": product["tags"].split("|"),
            "materials": product["materials"].split("|"),
        }

        url = f"{self.base_url}/listings/{listing_id}"
        response = requests.patch(url, headers=self._headers(), json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        print(f"Updated listing: {listing_id}")
        return data


def load_products_from_csv(path: str):
    """
    Read product rows from a CSV file.
    Each row is manually edited by me before running the script.

    Expected columns:
    action,listing_id,title,description,price,quantity,taxonomy_id,tags,materials
    """
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def main():
    # All credentials are stored as environment variables on my local machine.
    api_key = os.environ.get("ETSY_API_KEY")
    shop_id = os.environ.get("ETSY_SHOP_ID")
    access_token = os.environ.get("ETSY_ACCESS_TOKEN")

    if not api_key or not shop_id or not access_token:
        raise RuntimeError(
            "Missing Etsy credentials. Please set ETSY_API_KEY, ETSY_SHOP_ID, ETSY_ACCESS_TOKEN."
        )

    client = EtsyClient(api_key=api_key, shop_id=shop_id, access_token=access_token)

    csv_path = "products.csv"  # manually maintained file
    products = load_products_from_csv(csv_path)

    for product in products:
        action = product["action"].strip().lower()

        # I always control exactly which rows are created/updated
        # by editing the CSV before running this script.
        if action == "create":
            client.create_draft_listing(product)
        elif action == "update":
            listing_id = product.get("listing_id")
            if listing_id:
                client.update_listing(listing_id, product)
        else:
            print(f"Skipping row with unknown action: {action}")

        # Be nice to the API – small delay between requests.
        time.sleep(0.5)


if __name__ == "__main__":
    main()
