import requests
from bs4 import BeautifulSoup
    
INDEED_URL = "https://kr.indeed.com/jobs?q=Python"

def extract_indeed_pages():    
    # html을 요청
    result = requests.get(INDEED_URL)
    soup = BeautifulSoup(result.text, "html.parser")

    # class가 pagination인 div를 반환
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))
            
    max_page = pages[-1]
    
    return max_page
