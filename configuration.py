import os
basedir = os.path.abspath(os.path.dirname(__file__))


def configure_build(deploy_to, branch, env):
    job_settings = {'DEPLOY_TO': deploy_to,
                    'FRONTEND_BRANCH': branch,
                    'BACKEND_BRANCH': branch,
                    'RUN_TEST': False,
                    'DEPLOY_REPO_BRANCH': 'master',
                    'NPM_ARGS': 'production',
                    'GRUNT_ARGS': 'testing',
                    'DEPLOY_TO_S3': False,
                    'MIGRATE': False,
                    'ENV': env}
    return job_settings


jenkins_server = 'http://123123'
jenkins_user = '23123'
jenkins_pass = '123123123'


servers = {'feature1': ('feature1.address.com', 'branch', 'env'),
           'feature2': ('feature2.address.com', 'branch', 'env'),
           'test': ('test.address.com', 'branch', 'env'),
           'preproduction': ('preproduction.address.com', 'branch', 'env')}

storybook_server = 'http://storybook.dev.roundme.com/'

class Config(object):
    SECRET_KEY = 'omg-its-really-secret'
    BASENAME = 'qajenkins.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, BASENAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
