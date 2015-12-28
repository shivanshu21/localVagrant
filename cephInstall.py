import pexpect
import os
import re
import sys

ADMIN_NODE = 'admin'

#==================== PROGRAM FLOW ====================#
## Check whether this is the admin node
command = 'cat /etc/hostname'
ret = os.popen(command).read()
pattern = re.compile(ADMIN_NODE)
if pattern.match(ret):
    print "This is the admin node. Continuing..."
else:
    print "This is not the admin node. Cannot continue with CEPH installation here!"
    sys.exit(0)

## Start CEPH deployment
print "\n\n== Starting CEPH deployment =="
os.chdir('/home/vagrant')
print "Adding keys..."
command = "wget -q -O- 'https://download.ceph.com/keys/release.asc' | sudo apt-key add -"
os.system(command)
print "Adding the Ceph packages to your repository..."
command = "echo deb http://download.ceph.com/debian-hammer/ $(lsb_release -sc) main | sudo tee /etc/apt/sources.list.d/ceph.list"
os.system(command)
print "Installing CEPH deploy..."
command = "sudo apt-get -y update && sudo apt-get -y install ceph-deploy"
os.system(command)
command = "sudo apt-get -y install ntp"
os.system(command)

## Run the ceph deploy script
print "\n\n== Running CEPH deploy =="
command = 'mkdir ceph_cluster'
os.system(command)
os.chdir('/home/vagrant/ceph_cluster')

#### Initiate a cluster and get proper ceph.conf
print "======== Initiating a new cluster ========"
command = 'ceph-deploy new admin'
os.system(command)
command = 'sudo cp /vagrant/ceph.conf .'
os.system(command)
command = 'sudo chmod 0755 ./ceph.conf'
os.system(command)

#### Start installation of ceph binaries
print "======== Installing CEPH on each node ========"
command = 'ceph-deploy install admin node4 node5 node6'
os.system(command)

#### ST MON leader makes first mon to come up
print "======== Creating first monitor ========"
command = 'ceph-deploy mon create-initial'
os.system(command)

#### Create directories on which to run OSDs
print "======== Creating dirs and activating OSDs ========"
command = 'ssh node4 \"sudo mkdir /var/local/osd0\"'
os.system(command)
command = 'ssh node5 \"sudo mkdir /var/local/osd1\"'
os.system(command)
command = 'ssh node6 \"sudo mkdir /var/local/osd2\"'
os.system(command)
command = 'ceph-deploy osd prepare node4:/var/local/osd0 node5:/var/local/osd1 node6:/var/local/osd2'
os.system(command)
command = 'ceph-deploy osd activate node4:/var/local/osd0 node5:/var/local/osd1 node6:/var/local/osd2'
os.system(command)

#### Copying keyrings
command = 'ceph-deploy admin admin node4 node5 node6'
os.system(command)
command = 'sudo chmod +r /etc/ceph/ceph.client.admin.keyring'
os.system(command)
