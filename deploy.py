from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['188.166.185.151']
env.user='root'
env.password='server2'
env.forward_agent = True
#runenv.use_ssh_config = True

'''
def taska():
    run('whoami')
'''

def prepare():
    run ('eval ssh-agent $SHELL')
    run ('ssh-add -l')

def deploy():
    #prepare()
    code_dir = '/fab'
    print (run('pwd'))
    #code_dir ='/Users/harikrishnan/Documents/work/CI/fab'
    with settings(warn_only=True):
        print (run("test -d %s" % code_dir).failed,"adadsdadadd")
        if run("test -d %s" % code_dir).failed:
            run("git clone git@github.com:Harish1792/CI.git %s" % "fab/")
    #with cd(code_dir):
    #    run("git pull")
        #run("touch app.wsgi")
