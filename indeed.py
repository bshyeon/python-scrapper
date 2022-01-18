import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f"https://kr.indeed.com/jobs?q=python&rqf=1&limit={LIMIT}"

def extract_indeed_pages():    
    # html을 요청
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    # class가 pagination인 div를 반환
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))
            
    max_page = pages[-1]
    
    return max_page

def extract_jobs(html):
    title = html.find("h2", {"class": "jobTitle"}).find("span", title=True).string
    company = html.find("span", {"class": "companyName"}).string
    location = html.find("div", {"class": "companyLocation"}).string
    job_id = html["data-jk"]

    return {"title": title, "company": company, "location": location, "link": f"https://kr.indeed.com/jobs?q=python&l&vjk={job_id}"}

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={LIMIT*page}")
        soup = BeautifulSoup(result.text, "html.parser")
        # 직업 목록을 불러옴
        results = soup.find_all("a", {"class": "fs-unmask"})
        
        for result in results:
            job = extract_jobs(result)
            jobs.append(job)
            
    return jobs