from jenkins import Jenkins
from configuration import configure_build, jenkins_server, jenkins_user, jenkins_pass, storybook_server, servers
from app import models, db
import requests


def start_job(server_label, job_name):
    job_data = models.Servers.query.filter_by(label=server_label).first()
    job_settings = configure_build(job_data.address,
                                   job_data.branch,
                                   job_data.env)
    server = Jenkins(jenkins_server, jenkins_user, jenkins_pass)
    server.build_job(job_name, job_settings)
    return "task planned"


def list_servers():
    servers_response = models.Servers.query.all()
    servers_dict = {}
    for e in servers_response:
        server = {e.label: (e.address, e.branch, e.env)}
        servers_dict.update(server)
    return servers_dict


def build_storybook(branch):
    job_settings = {'BRANCH': branch}
    server = Jenkins(jenkins_server, jenkins_user, jenkins_pass)
    server.build_job('Roundme.StoryBook.Build', job_settings)


def write_server(server_info):
    db.session.add(server_info)
    db.session.commit()
    # print("Job Edit {} {} {}".format(server_id, deploy_to, branch))


def create_server(server_label, deploy_to, branch, env):
    job_data = models.Servers()
    job_data.label = server_label
    job_data.address = deploy_to
    job_data.branch = branch
    job_data.env = env
    write_server(job_data)



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
