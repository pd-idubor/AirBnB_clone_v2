#!/usr/bin/python3
"""Script compressing files into an archive"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create archive with add web_static files"""
    if not os.path.exists("versions"):
        os.mkdir("versions")

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(now)
    path = "versions/{}".format(name)

    local("tar -cvzf {} web_static".format(path))

    if os.path.exists(path):
        return path
    return None
