import requests
from bs4 import BeautifulSoup

from indeed import extract_jobs

URL = f"https://stackoverflow.com/jobs?q=python&pg=1"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("span")
    last_page = pages[-2].get_text()
    return int(last_page)

def extract_job(html):
    title = html.find("a", {"class": "s-link"})["title"]
    company = html.find("h3", {"class": "mb4"}).find("span").string
    location = html.find("h3", {"class": "mb4"}).find("span", {"class": "fc-black-500"}).string.strip()
    link = html["data-jobid"]
    print(title, company, location)
    return {"title": title, "company": company, "location": location, "link": f"https://stackoverflow.com/jobs?id={link}"}

def extract_jobs(last_page):
    jobs =[]
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs    

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs