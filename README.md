# uploadinglists
uploadinglists – Internal Etsy Listing Helper

This repository contains a small internal tool I built to help me manage my own Etsy shop more efficiently.
It is not a public app, and I am the only user.
The purpose of the tool is to reduce repetitive manual work when creating and updating listings.

What the tool does
The script reads product data from a manually prepared CSV file (products.csv) and performs two actions:
1. Create draft listings
• The tool sends product information (title, description, tags, price, materials, etc.) to the Etsy API
• All new listings are created in draft state only
• I always review and publish them manually inside Etsy

2. Update existing listings
• The tool can update titles, descriptions, tags, price, or quantity
• Only for listings I manually specify with a listing ID
• No automatic publishing or automated actions

Example CSV Input
I manually edit this file before running the script:
action,listing_id,title,description,price,quantity,taxonomy_id,tags,materials
action = create or update
I decide exactly which listings to process
Nothing runs automatically without my approval

Credentials
All Etsy credentials (ETSY_API_KEY, ETSY_SHOP_ID, ETSY_ACCESS_TOKEN) are stored as local environment variables.
No credentials are shared or exposed in this repository.

Usage
Run:
python3 main.py

The script will process each row from products.csv and:
✔ Create draft listings
✔ Update existing listings
✔ Skip anything not marked clearly with an action
A short delay is added between API calls to respect rate limits.

Important Notes
This tool is for my personal shop only
No other users can access or use it
It does not auto-publish listings
It does not automate content creation — I manually prepare all data
It simply speeds up repetitive tasks I normally do in Etsy

Files in this repository
main.py – Python script that interacts with the Etsy API
products.csv – (ignored in public repo, created locally) contains my manually prepared data
README.md – documentation explaining the purpose of the tool
