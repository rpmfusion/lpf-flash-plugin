#!/usr/bin/python3

""" Warning not complete """

import requests
import re
import os
import subprocess

def runme(cmd, env, cwd='.'):
    """Simple function to run a command and return 0 for success, 1 for
       failure.  cmd is a list of the command and arguments, action is a
       name for the action (for logging), pkg is the name of the package
       being operated on, env is the environment dict, and cwd is where
       the script should be executed from."""
    try:
        subprocess.check_call(cmd, env=env, cwd=cwd) #, stderr=None
    except subprocess.CalledProcessError as e:
        sys.stderr.write('%s failed: %s\n' % (cmd, e))
        return 1
    return 0

html = requests.get('http://get.adobe.com/flashplayer/about/')
#print (html.text)

spec = open('flash-plugin.spec.in').read()
str_mx3 = re.compile('Version:\s*([\d.]+)')
res2 = str_mx3.findall(spec)
old_version = res2[-1]
print ("old_version = %s" % old_version)

str_mx = re.compile('Linux.*?Firefox.*?NPAPI.*?<td>([\d.]+)<.td>', re.S)
res = str_mx.findall(html.text)
new_version = res[-1]
print ("new_version = %s" % new_version)

if new_version != old_version:
    enviro = os.environ
    pkgcmd = ['rpmdev-bumpspec', '-n', new_version, '-c', 'Update to %s' % (new_version), 'flash-plugin.spec.in']
    if runme(pkgcmd, enviro):
        print('error running runme')
    pkgcmd = ['rpmdev-bumpspec', '-n', new_version, '-c', 'Update to %s' % (new_version), 'lpf-flash-plugin.spec'] # 2>/dev/null
    if runme(pkgcmd, enviro):
        print('error running runme')

    print('rfpkg ci -c && git show')
    print('rfpkg push && rfpkg build --nowait')
    print('git checkout f30 && git merge master && git push && rfpkg build --nowait; git checkout master')
    print('git checkout f29 && git merge master && git push && rfpkg build --nowait; git checkout master')
    #print('git checkout f28 && git merge master && git push && rfpkg build --nowait; git checkout master')

else:
    print("Already updated !")
