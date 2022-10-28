#!/usr/bin/python3
"""Compress web static package
"""
import os.path
from fabric.api import *

env.hosts = ["44.210.236.120", "34.204.181.124"]


def do_deploy(archive_path):
    """
    deploying an archive to a server
    """
    if not exists(archive_path):
        return False
    try:
        archive_fname = archive_path.split('/')[-1]
        archive_bname = archive_fname.split('.')[0]
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(archive_bname))
        run('tar -xzf /tmp/{0}.tgz -C /data/web_static/releases/{0}'.format(
                    archive_bname))
        run(('mv /data/web_static/releases/{0}/web_static/* ' +
            '/data/web_static/releases/{0}/').format(archive_bname))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            archive_bname))
        run('rm -f /tmp/{}'.format(archive_fname))
        run('rm -f /data/web_static/current')
        run(('ln -s /data/web_static/releases/{}' +
            ' /data/web_static/current').format(archive_bname))
        return True
    except Exception:
        return False
