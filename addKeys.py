#!/bin/python

## ===========================================
## This is supposed to run inside every VM
## provisioned by Vagrant for CEPH deployment
## ===========================================

import keysLib

keysLib.genKey()
keysLib.copyKey("node4")
keysLib.copyKey("node5")
keysLib.copyKey("node6")
keysLib.copyKey("admin")
