# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "trusty64"
  config.vm.provision "shell", path: "setup.sh"

  config.vm.define "node4" do |node4|
    node4.vm.network :forwarded_port, guest: 80, host: 8080
    node4.vm.network :private_network, ip: "192.168.33.10"
    node4.vm.provider :virtualbox do |vb|
      vb.gui = false
      vb.customize ["modifyvm", :id, "--memory", "512"]
      vb.customize ["modifyvm", :id, "--cpus", "1"]
    end
    node4.vm.provision "shell", inline: "echo node4 | sudo tee /etc/hostname"
    node4.vm.provision "shell", inline: "sudo service hostname restart"
  end

  config.vm.define "node5" do |node5|
    node5.vm.network :forwarded_port, guest: 80, host: 8081
    node5.vm.network :private_network, ip: "192.168.33.11"
    node5.vm.provider :virtualbox do |vb|
      vb.gui = false
      vb.customize ["modifyvm", :id, "--memory", "512"]
      vb.customize ["modifyvm", :id, "--cpus", "1"]
    end
    node5.vm.provision "shell", inline: "echo node5 | sudo tee /etc/hostname"
    node5.vm.provision "shell", inline: "sudo service hostname restart"
  end

  config.vm.define "node6" do |node6|
    node6.vm.network :forwarded_port, guest: 80, host: 8082
    node6.vm.network :private_network, ip: "192.168.33.12"
    node6.vm.provider :virtualbox do |vb|
      vb.gui = false
      vb.customize ["modifyvm", :id, "--memory", "512"]
      vb.customize ["modifyvm", :id, "--cpus", "1"]
    end
    node6.vm.provision "shell", inline: "echo node6 | sudo tee /etc/hostname"
    node6.vm.provision "shell", inline: "sudo service hostname restart"
  end

  config.vm.define "node7" do |node7|
    node7.vm.network :forwarded_port, guest: 80, host: 8083
    node7.vm.network :private_network, ip: "192.168.33.13"
    node7.vm.provider :virtualbox do |vb|
      vb.gui = false
      vb.customize ["modifyvm", :id, "--memory", "512"]
      vb.customize ["modifyvm", :id, "--cpus", "1"]
    end
    node7.vm.provision "shell", inline: "echo admin | sudo tee /etc/hostname"
    node7.vm.provision "shell", inline: "sudo service hostname restart"
  end

end
