from __future__ import with_statement
from fabric.api import settings, run, cd

def deploy():
    code_dir = '/srv/vhosts/support/'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone git@github.com:azpm/azpm-www-support.git %s" % code_dir)
            run("setfacl -m d:g:http_srv:rwx %slogs")

    with cd(code_dir):
        run("git pull")

    load_config()

def restart_site():
    working_dir = '/srv/vhosts/support/public'
    with cd(working_dir):
        run("touch run.wsgi")

def load_config(mode="production"):
    working_dir = '/srv/vhosts/'
    with cd(working_dir):
        run("cp deployment/{0:>s}/support/local_settings.py support/project/".format(mode))