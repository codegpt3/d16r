# -*- coding: utf-8 -*-
from fabric.api import env, put, run, task, roles, sudo, cd

env.roledefs = {
    'ds_001': ['101.34.233.54'],
    'ds_002': ['101.34.233.54'],
    'ds_003': ['101.34.233.54']
}

env.abort_on_prompts = True
env.key_filename = 'entry.key'
env.gateway = '101.34.233.54'
env.user = 'root'


@task
@roles('ds_001')
def ds_001():
    run(f'mkdir -p ~/{env.user}/ds')
    put('./ds/001/*', f'~/{env.user}/ds')
    with cd(f'~/{env.user}/ds'):
        sudo('cp env .env')
        # sudo('docker-compose -f docker-compose-001.yml down || true')
        # sudo('docker-compose -f docker-compose-001.yml up -d')


@task
@roles('ds_002')
def ds_002():
    run(f'mkdir -p ~/{env.user}/ds')
    put('./ds/002/*', f'~/{env.user}/ds')
    with cd(f'/home/{env.user}/ds'):
        sudo('cp env .env')
        sudo('docker-compose -f docker-compose-002.yml down || true')
        sudo('docker-compose -f docker-compose-002.yml up -d')


@task
@roles('ds_003')
def ds_003():
    run(f'mkdir -p /home/{env.user}/ds')
    put('services/ds/003/*', f'/home/{env.user}/ds')
    with cd(f'/home/{env.user}/ds'):
        sudo('cp env .env')
        sudo('docker-compose -f docker-compose-003.yml down || true')
        sudo('docker-compose -f docker-compose-003.yml up -d')
