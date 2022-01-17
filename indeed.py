import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f"https://kr.indeed.com/jobs?q=Python&rqf=1&limit={LIMIT}"

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

def extract_indeed_jobs(last_pages):
    jobs = []
    for page in range(last_pages):
        result = requests.get(f"{URL}&start={LIMIT*page}")
        print(result.status_code)
        
    return jobs