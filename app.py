from flask import Flask, render_template, jsonify, request 
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

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

@app.route("/job/<id>")
def show_job(id):   
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job=job)

@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id):
    data = request.form
    job = load_job_from_db(id)
    print(id)
    print(data)
    add_application_to_db(id, data)

    return render_template('application_submitted.html', 
                           application=data,
                           job=job)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=7000, debug=True)
