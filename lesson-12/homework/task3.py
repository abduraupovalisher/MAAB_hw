import requests
from bs4 import BeautifulSoup
import json

def scrape_laptops():
    url = "https://www.demoblaze.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    laptops = []
    products = soup.find_all("div", class_="card-block")
    
    for product in products:
        name = product.find("h4", class_="card-title").text.strip()
        price = product.find("h5").text.strip()
        description = product.find("p", class_="card-text").text.strip()
        
        laptops.append({
            "name": name,
            "price": price,
            "description": description
        })
    
    return laptops

def save_to_json(laptops, filename="laptops.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(laptops, file, indent=4)

if __name__ == "__main__":
    laptop_data = scrape_laptops()
    save_to_json(laptop_data)

