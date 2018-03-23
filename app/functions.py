from jenkins import Jenkins
from configuration import configure_build, jenkins_server, jenkins_user, jenkins_pass, storybook_server, servers
# from app import models
import requests

def start_job(server_id, job_name):
    # job_data = models.Servers.query.filter_by(id=server_id).first()
    job_data = servers[server_id]
    job_settings = configure_build(job_data[0],
                                   job_data[1],
                                   job_data[2])
    server = Jenkins(jenkins_server, jenkins_user, jenkins_pass)
    server.build_job(job_name, job_settings)
    print(job_data)
    return "task planned"


def build_storybook(branch):
    job_settings = {'BRANCH': branch}
    server = Jenkins(jenkins_server, jenkins_user, jenkins_pass)
    server.build_job('Roundme.StoryBook.Build', job_settings)


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


def get_storybooks():
    storybooks_list = []
    r = requests.get(storybook_server)
    response = r.text.split('a href="')
    for i in response:
        i = i.split('">')[0]
        if i != 'fonts/' and i != 'images/':
            storybooks_list.append(i)
    storybooks_list = storybooks_list[2:]
    return storybooks_list
