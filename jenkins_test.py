from jenkins import Jenkins


job_settings = {'DEPLOY_TO': 'feature1.dev.roundme.com',
                'FRONTEND_BRANCH': '1.6.1',
                'BACKEND_BRANCH': '1.6.1',
                'RUN_TEST': False,
                'DEPLOY_REPO_BRANCH': 'master',
                'NPM_ARGS': 'production',
                'GRUNT_ARGS': 'testing',
                'DEPLOY_TO_S3': False,
                'MIGRATE': False,
                'ENV': 'feature'}

server = Jenkins('http://234234', username='234', password='234234')

# serverstring
print(server)
user = server.get_whoami()
print(user)
job = server.get_job_config('Roundme.Full.Build')
print(job)
server.build_job('Roundme.Full.Build', job_settings)
last_build_number = server.get_job_info('Roundme.Full.Build')['lastCompletedBuild']['number']
build_info = server.get_build_info('Roundme.Full.Build', last_build_number)
print(build_info)
