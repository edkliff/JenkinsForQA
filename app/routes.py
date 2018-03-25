from app import app
from flask import redirect, render_template
from app.forms import BuildStorybook, Server
from app.functions import get_storybooks, build_storybook, start_job, create_server, list_servers
from app.functions import write_server
from configuration import storybook_server
from app.models import Servers


@app.route('/')
def index():
    return render_template('base.html')


# Logs
@app.route('/messages')
def messages():
    """
    Logs
    :return: list of logs
    """
    return render_template('messages.html', title='Messages',
                           domain='all')


@app.route('/storybooks',  methods=['GET', 'POST'])
def storybooks():
    form = BuildStorybook()
    storybooks = get_storybooks()
    if form.validate_on_submit():
        build_storybook(form.branch.data)
    return render_template('storybooks.html', title='Storybooks', form=form,
                           storyserver=storybook_server,storybooks=storybooks)


@app.route('/servers')
def servers_list():
    servers = list_servers()
    return render_template('servers.html', title='Servers', servers=servers)


@app.route('/run/<server>', methods=['GET', 'POST'])
def edit_account(server):
    start_job(server, 'Roundme.Full.Build')
    return redirect('/servers')


@app.route('/add', methods=['GET', 'POST'])
def add_server():
    form = Server()
    if form.validate_on_submit():
        create_server(form.label.data, form.address.data,
                      form.branch.data, form.env.data)
    return render_template('create_server.html', title='Create Server', form=form)


@app.route('/edit/<server>', methods=['GET', 'POST'])
def edit_server(server):
    form = Server()
    job_data = Servers.query.filter_by(label=server).first()
    if form.validate_on_submit():
        job_data.label = form.label.data
        job_data.address = form.address.data
        job_data.branch = form.branch.data
        job_data.env = form.env.data
        write_server(job_data)
        return redirect('/servers')
    form.label.data = job_data.label
    form.address.data = job_data.address
    form.branch.data = job_data.branch
    form.env.data = job_data.env
    return render_template('create_server.html', title='Create Server', form=form)
