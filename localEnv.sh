##export http_proxy=""
##export https_proxy=$http_proxy
##export no_proxy="localhost,127.0.0.1"

## Copy http proxy as DNS server in /etc/resolv.conf
## echo "nameserver <IP>" | sudo tee -a /etc/resolv.conf

## Copy the apt.conf in /etc/apt/apt.conf
## DO NOT FORGET TO MODIFY apt.conf in current dir
## sudo cp /vagrant/apt.conf /etc/apt/

## Modify ceph.conf to change mon node initial IP
## Modify ceph.conf to change keystone settings
