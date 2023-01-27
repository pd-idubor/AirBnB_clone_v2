#!/usr/bin/python3
"""Script compressing files into an archive"""
import os
from datetime import datetime
from fabric.api import *

env.hosts = ['54.237.29.20', '54.236.47.104']


def do_pack():
    """Create archive with add web_static files"""
    if not os.path.exists("versions"):
        os.mkdir("versions")

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(now)
    archive_path = "versions/{}".format(name)

    local("tar -cvzf {} web_static".format(path))

    if os.path.exists(path):
        return path
    return None


def do_deploy(archive_path):
    """Deploys archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    name = os.path.basename(archive_path)
    arch_name = os.path.splitext(name)[0]
    tmp_dir = '/tmp/'
    release_dir = '/data/web_static/releases/'
    release_path = release_dir + arch_name + '/'
    sym_dir = '/data/web_static/current'

    put(archive_path, tmp_dir + name)
    run('mkdir -p ' + release_path)
    run('tar -xzf ' + tmp_dir + name + ' -C ' + release_path)
    run('rm ' + tmp_dir + name)
    run('mv ' + release_path + 'web_static/* ' + release_path)
    run('rm -rf ' + release_path + 'web_static')
    run('rm -rf ' + sym_dir)
    run('ln -s ' + release_path + ' ' + sym_dir)
    return True


def deploy():
    """Creates and distributes archives to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
