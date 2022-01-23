from functools import reduce
from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file
from flask import Flask, render_template, request, redirect

# Flask
app = Flask("SuperScarapper")

db = {}

@app.route("/")
def home():
    # render_template를 import한 후 해당 html파일 반환
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get("word").lower()
    fromDb = db.get(word)
    if word:
        if fromDb:
            jobs = fromDb
        else:
            jobs = get_so_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", word=word, resultsNumber = len(jobs), jobs=jobs)

app.run(host="127.0.0.1")