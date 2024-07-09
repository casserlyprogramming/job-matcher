from flask import Flask, jsonify
from api import get_members, get_jobs
from member import Member

app = Flask(__name__)

@app.route("/")
def show_job_mathces():
    members = get_members()
    jobs = get_jobs()
    return_json = []
    for member in members:
        m = Member(member)
        m.assign_potential_jobs(jobs)
        return_json.append({
            "name": m.name,
            "jobs": m.jobs
        })

    return jsonify(return_json)
