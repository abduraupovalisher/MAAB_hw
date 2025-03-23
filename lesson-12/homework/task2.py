import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    job_listings = []
    jobs = soup.find_all("div", class_="card-content")
    
    for job in jobs:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="description").text.strip()
        link = job.find("a")['href']
        
        job_listings.append((title, company, location, description, link))
    
    return job_listings

def store_jobs_in_db(job_listings):
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
    
    for job in job_listings:
        cursor.execute("""
            INSERT OR IGNORE INTO jobs (title, company, location, description, link)
            VALUES (?, ?, ?, ?, ?)
        """, job)
    
    conn.commit()
    conn.close()

def export_jobs_to_csv(filename="jobs.csv", location_filter=None, company_filter=None):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    
    query = "SELECT title, company, location, description, link FROM jobs"
    params = []
    
    if location_filter:
        query += " WHERE location = ?"
        params.append(location_filter)
    elif company_filter:
        query += " WHERE company = ?"
        params.append(company_filter)
    
    cursor.execute(query, params)
    jobs = cursor.fetchall()
    
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(jobs)
    
    conn.close()

if __name__ == "__main__":
    jobs = scrape_jobs()
    store_jobs_in_db(jobs)
    export_jobs_to_csv()

