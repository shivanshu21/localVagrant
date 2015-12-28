import pexpect
import os
import re
import sys

PASSWORD = 'vagrant'
TIMEOUT  = 10

#==================== FUNCTION DEFINITIONS ====================#
def genKey():
    child = pexpect.spawn('ssh-keygen')
    child.expect('Enter.*: ', TIMEOUT)
    child.sendline()
    ret = child.expect(['Enter passphrase.*: ', '.*Overwrite.*'], TIMEOUT)
    if ret == 0:
        child.sendline()
    elif ret == 1:
        child.sendline('y')
        child.expect('Enter passphrase.*: ')
        child.sendline()
    child.expect('Enter same passphrase.*: ', TIMEOUT)
    child.sendline()
    print child.before
    try:
        child.interact()
    except:
        print "Unexpected error during keypair generation"
    return 0

def copyKey(node):
    command_str = 'ssh-copy-id ' + node
    child = pexpect.spawn(command_str)
    ret = child.expect(['Are you sure.*', '.*password: ', '.*All keys were skipped.*'], TIMEOUT)
    if ret == 0:
        child.sendline('yes')
        ret = child.expect(['.*password: ', '.*All keys were skipped.*'], TIMEOUT)
        if ret == 0:
            child.sendline(PASSWORD)
        elif ret == 1:
            pass
    elif ret == 1:
        child.sendline(PASSWORD)
    elif ret == 2:
        pass
    else:
        print "Unexpected prompt during copying keys"
    print child.before
    try:
        child.interact()
    except:
        print "Unexpected error has occured during copying keys"
    return 0

def sshLogin(node, command):
    command_str = 'ssh vagrant@' + node + ' ' + command
    print "sshLogin: Sending command: " + command_str
    child = pexpect.spawn(command_str)
    ret = child.expect(['.*password:.*', '.*continue connecting.*'], 100 * TIMEOUT)
    if ret == 0:
        child.sendline(PASSWORD)
    elif ret == 1:
        child.sendline('yes')
        child.expect('.*password:.*', 100 * TIMEOUT)
        child.sendline(PASSWORD)
    return

#==============================================================#


