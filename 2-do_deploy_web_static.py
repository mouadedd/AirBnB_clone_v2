#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['34.227.89.197', '100.25.20.169']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """the file at the path archive_path
    """
    try:
        if not (path.exists(archive_path)):
            return False
        put(archive_path, '/tmp/')

        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
            .format(timestamp))

        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
    except:
        return False
    return True
