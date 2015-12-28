#! /usr/bin/python

## ===========================================
## Builds four nodes and installs CEPH inside
## them
## ===========================================

import pexpect
import os
import re
import sys
import keysLib

## Make four Vagrant VMs
print "\n\nMaking four VMs..."
command = "vagrant up"
os.system(command)

## From the host machine, login to these machines and run addKeys
## addKeys will make sure these machines can do a sudoless ssh
## to and from each other
print "\n\nCopying Keys..."
keysLib.sshLogin("192.168.33.10", "python /vagrant/addKeys.py")
keysLib.sshLogin("192.168.33.11", "python /vagrant/addKeys.py")
keysLib.sshLogin("192.168.33.12", "python /vagrant/addKeys.py")
keysLib.sshLogin("192.168.33.13", "python /vagrant/addKeys.py")

## Install CEPH
print "\n\nInstalling..."
keysLib.sshLogin("192.168.33.13", "python /vagrant/cephInstall.py")
