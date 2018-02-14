from jenkins import Jenkins
from configuration import configure_build
from app import models

def start_job(id):
    job_data = models.Servers.query.filter_by(id=id).first()
    print(job_data)