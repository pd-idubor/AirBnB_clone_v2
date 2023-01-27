#!/usr/bin/python3
"""Script that deploys archives to web server"""
import os.path
from datetime import datetime
from fabric.api import local, put, run


def do_pack():
    """Create archive with add web_static files"""
    if not os.path.exists("versions"):
        os.mkdir("versions")

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(now)
    archive_path = "versions/{}".format(name)

    local("tar -cvzf {} web_static".format(archive_path))

    if os.path.exists(archive_path):
        return archive_path
    return None


def do_deploy(archive_path):
    """Deploy archives"""

    archive = os.path.basename(archive_path)
    arch_name= os.path.splitext(archive)[0]
    tmp_dir = "/tmp/"
    put(archive_path, tmp_dir + archive)

    dest_dir = "/data/web_static/releases/"
    dest_path = dest_dir + arch_name + "/"
    run('mkdir -p ' + dest_path)
    run('tar -zxf ' + tmp_dir + archive + ' -C ' + dest_path)
    run('rm ' + tmp_dir + archive)
    run('mv ' + dir_path + 'web_static/* ' + dir_path)
    run('rm -rf ' + dir_path + 'web_static')

    link_dir = '/data/web_static/current'
    run('rm -rf ' + link_dir)
    run('ln -s ' + dir_path + ' ' + link_dir)
    return True
