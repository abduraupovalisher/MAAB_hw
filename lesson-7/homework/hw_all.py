from bs4 import BeautifulSoup
import sqlite3
import json
import requests
import csv

def scrape_weather():
    with open("weather.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    weather_data = []
    rows = soup.find("table").find("tbody").find_all("tr")
    
    for row in rows:
        cols = row.find_all("td")
        day = cols[0].text.strip()
        temp = int(cols[1].text.replace("°C", "").strip())
        condition = cols[2].text.strip()
        weather_data.append({"day": day, "temperature": temp, "condition": condition})
    
    return weather_data

def analyze_weather(data):
    highest_temp = max(data, key=lambda x: x['temperature'])
    sunny_days = [entry["day"] for entry in data if entry["condition"].lower() == "sunny"]
    avg_temp = sum(entry["temperature"] for entry in data) / len(data)
    
    print("Weather Forecast:")
    for entry in data:
        print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")
    
    print("\nAnalysis:")
    print(f"Highest Temperature: {highest_temp['temperature']}°C on {highest_temp['day']}")
    print(f"Sunny Days: {', '.join(sunny_days)}")
    print(f"Average Temperature: {avg_temp:.2f}°C")

weather_data = scrape_weather()
analyze_weather(weather_data)

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    job_listings = []
    jobs = soup.find_all("div", class_="card-content")
    
    for job in jobs:
        title = job.find("h2", class_="title is-5").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="content").text.strip()
        link = job.find("a")['href']
        
        job_listings.append({
            "title": title,
            "company": company,
            "location": location,
            "description": description,
            "link": link
        })
    
    return job_listings

def store_jobs_in_db(jobs):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            link TEXT,
            UNIQUE(title, company, location)
        )
    """)
    
    for job in jobs:
        cursor.execute("""
            INSERT OR IGNORE INTO jobs (title, company, location, description, link)
            VALUES (?, ?, ?, ?, ?)
        """, (job['title'], job['company'], job['location'], job['description'], job['link']))
    
    conn.commit()
    conn.close()

def filter_jobs(location=None, company=None):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

def export_jobs_to_csv(filename="filtered_jobs.csv", location=None, company=None):
    jobs = filter_jobs(location, company)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Company", "Location", "Description", "Link"])
        writer.writerows(jobs)
    print(f"Filtered jobs exported to {filename}")

job_data = scrape_jobs()
store_jobs_in_db(job_data)

def scrape_laptops():
    url = "https://www.demoblaze.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    laptops = []
    products = soup.find_all("div", class_="card")
    
    for product in products:
        name = product.find("h4", class_="card-title").text.strip()
        price = product.find("h5").text.strip()
        description = product.find("p", class_="card-text").text.strip()
        
        laptops.append({"name": name, "price": price, "description": description})
    
    with open("laptops.json", "w", encoding="utf-8") as file:
        json.dump(laptops, file, indent=4)
    
    print("Laptop data saved to laptops.json")

scrape_laptops()
