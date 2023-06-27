from flask import Flask, render_template, jsonify 
from database import load_jobs_from_db

app = Flask(__name__)

#retrieving the sql database 
jobs = load_jobs_from_db()

@app.route("/")
def hello_jovian():
    return render_template('home.html', jobs=jobs, 
                           company_name = "Jovian")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=7000, debug=True)
