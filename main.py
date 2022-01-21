from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file
from flask import Flask

#indeed_jobs = get_indeed_jobs()
#so_jobs = get_so_jobs()
#jobs = indeed_jobs + so_jobs

# save_to_file(jobs)

app = Flask("SuperScarapper")

@app.route("/")
def home():
    return "Hello! Welcome my homepage"

@app.route("/contact")
def contact():
    return "Contact Page"

app.run(host="127.0.0.1")