# uploadinglists – Internal Etsy Listing Helper

This repository contains a small **internal tool** I built to help me manage my own Etsy shop more efficiently.  
It is **not a public app**, and I am the only user.  
The purpose of the tool is to reduce repetitive manual work when creating and updating listings.

---

## What the tool does

The script reads product data from a **manually prepared CSV file** (`products.csv`) and performs two actions:

### 1️⃣ Create **draft** listings
- Sends product information (title, description, tags, price, materials, etc.) to the Etsy API  
- All listings are created in **draft** state  
- I always review and publish them manually inside Etsy

### 2️⃣ Update existing listings
- Can update titles, descriptions, tags, prices, or quantities  
- Works only for listing IDs that I manually specify  
- No auto-publishing or automated action without my input

---

## Example CSV Input

I manually edit this file before running the script:
action,listing_id,title,description,price,quantity,taxonomy_id,tags,materials


- `action` = `create` or `update`  
- I choose exactly which rows to process  
- Nothing runs automatically

---

## Credentials

All Etsy credentials (`ETSY_API_KEY`, `ETSY_SHOP_ID`, `ETSY_ACCESS_TOKEN`) are stored as **local environment variables**.  
No credentials are exposed or stored in this repository.

---

## Usage

Run the tool:

```bash
python3 main.py


