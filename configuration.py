import os
basedir = os.path.abspath(os.path.dirname(__file__))

def configure_build(deploy_to, branch):
    job_settings = {'DEPLOY_TO': deploy_to,
                    'FRONTEND_BRANCH': branch,
                    'BACKEND_BRANCH': branch,
                    'RUN_TEST': False,
                    'DEPLOY_REPO_BRANCH': 'master',
                    'NPM_ARGS': 'production',
                    'GRUNT_ARGS': 'testing',
                    'DEPLOY_TO_S3': False,
                    'MIGRATE': False,
                    'ENV': 'feature'}
    return job_settings


class Config(object):
    SECRET_KEY = 'omg-its-really-secret'
    BASENAME = 'qajenkins.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, BASENAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
