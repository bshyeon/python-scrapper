from gettext import find
import requests
from bs4 import BeautifulSoup

# html을 요청
indeed_result = requests.get("https://kr.indeed.com/jobs?q=Python")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

# class가 pagination인 div를 반환
pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all("a")
pages = []

for link in links[:-1]:
    pages.append(int(link.string))
        
max_page = pages[-1]