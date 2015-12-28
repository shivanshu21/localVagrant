sudo -i
source /vagrant/localEnv.sh

echo "========================== Installing software"
apt-get -y update
apt-get -y install git
apt-get -y install screen
apt-get -y install python-boto
apt-get -y install python-pip
sudo pip install pexpect

echo "========================== Making directories"
mkdir /root/gitcode
cd /root/gitcode

echo "========================== Getting Git code and running"
git config --global user.name "Shivanshu Goswami"
git config --global user.email "shivanshu.goswami@ril.com"
git clone https://github.com/shivanshu21/prac0.git
cd prac0
chmod 755 cprcfil.sh
./cprcfil.sh

echo "========================= Adding passwordless SSH capabilities"
echo "## Vagrant CEPH user" | sudo tee -a /etc/hosts
echo "192.168.33.10      node4" | sudo tee -a /etc/hosts
echo "192.168.33.11      node5" | sudo tee -a /etc/hosts
echo "192.168.33.12      node6" | sudo tee -a /etc/hosts
echo "192.168.33.13      node7" | sudo tee -a /etc/hosts
echo "192.168.33.13      admin" | sudo tee -a /etc/hosts
sudo cp /vagrant/ssh_config /home/vagrant/.ssh
sudo mv /home/vagrant/.ssh/ssh_config /home/vagrant/.ssh/config
sudo cp /vagrant/ssh_config /root/.ssh
sudo mv /root/.ssh/ssh_config /root/.ssh/config
