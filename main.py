from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file
from flask import Flask, render_template

#indeed_jobs = get_indeed_jobs()
#so_jobs = get_so_jobs()
#jobs = indeed_jobs + so_jobs

# save_to_file(jobs)


# Flask
app = Flask("SuperScarapper")

@app.route("/")
def home():
    # render_template를 import한 후 해당 html파일 반환
    return render_template("index.html")

@app.route("/<username>")
def contact(username):
    return f"Hello your name is {username}"

app.run(host="127.0.0.1")