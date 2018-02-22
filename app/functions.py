from jenkins import Jenkins
from configuration import configure_build, jenkins_server, jenkins_user, jenkins_pass
from app import models


def start_job(server_id):
    job_data = models.Servers.query.filter_by(id=server_id).first()
    job_settings = configure_build(job_data.address,
                                   job_data.branch)
    server = Jenkins(jenkins_server, jenkins_user, jenkins_pass)
    server.build_job('Roundme.Full.Build', job_settings)
    print(job_data)
    return "task planned"


def edit_server(server_id, deploy_to, branch):
    print("Job Edit {} {} {}".format(server_id, deploy_to, branch))


def create_server(deploy_to, branch):
    print("Job Create {} {}".format(deploy_to, branch))


def create_user(username):
    print("Create user {}".format(username))


def block_user(username):
    print("Block User {}".format(username))


def change_password(username, password):
    print("Change Password {} {}".format(username, password))
