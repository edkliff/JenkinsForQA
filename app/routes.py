from app import app
from flask import redirect, render_template
from app.forms import BuildStorybook
from app.functions import get_storybooks, build_storybook
from configuration import storybook_server, servers

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
        print('azaza {}'.format(form.branch.data))
    return render_template('storybooks.html', title='Storybooks', form=form,
                           storyserver=storybook_server,storybooks=storybooks)


@app.route('/servers')
def servers_list():
    return render_template('servers.html', title='Servers', servers=servers)
