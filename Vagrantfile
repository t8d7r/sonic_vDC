# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
SP_number = 2
LF_number = 4
SRV_per_leaf_pair = 2
Vagrant.configure("2") do |config|
  config.ssh.username = "admin"
  config.ssh.password = "YourPaSsWoRd"

  (1..SP_number).each do |i|
    config.vm.define "spine#{i}" do |sw|
      sw.vm.synced_folder ".", "/vagrant", disabled: true
      sw.vm.box = "sonic"
      (1..LF_number).each do |j|
        sw.vm.network :private_network,
	  :libvirt__tunnel_type => "udp",
	  :libvirt__tunnel_local_ip => "127.0.10.#{i}" ,
	  :libvirt__tunnel_local_port => "100#{j}",
	  :libvirt__tunnel_ip => "127.0.20.#{j}",
          :libvirt__tunnel_port => "100#{i}",
	  :libvirt__iface_name => "eth#{j}",
          auto_config: false
        end
      ((LF_number+1)..24).each do |j|
        sw.vm.network :private_network,
          :libvirt__tunnel_type => "udp",
          :libvirt__tunnel_local_ip => "127.0.10.#{i}" ,
          :libvirt__tunnel_local_port => "100#{j}",
          :libvirt__tunnel_ip => "127.99.20.#{j}",
          :libvirt__tunnel_port => "9999",
          :libvirt__iface_name => "eth#{j}",
	auto_config: false
        end
    end
  end
  (1..LF_number).each do |i|
    config.vm.define "leaf#{i}" do |sw|
      sw.vm.synced_folder ".", "/vagrant", disabled: true
      sw.vm.box = "sonic"
      (1..SP_number).each do |j|
        sw.vm.network :private_network,
          :libvirt__tunnel_type => "udp",
          :libvirt__tunnel_local_ip => "127.0.20.#{i}" ,
          :libvirt__tunnel_local_port => "100#{j}",
          :libvirt__tunnel_ip => "127.0.10.#{j}",
          :libvirt__tunnel_port => "100#{i}",
          :libvirt__iface_name => "eth#{j}",
          auto_config: false
      end
      (SP_number+1..SP_number+SRV_per_leaf_pair).each do |j|
        sw.vm.network :private_network,
          :libvirt__tunnel_type => "udp",
          :libvirt__tunnel_local_ip => "127.0.20.#{i}" ,
          :libvirt__tunnel_local_port => "100#{j}",
          :libvirt__tunnel_ip => "127.0.30.#{(i+(i%2))/2}#{j-SP_number}",
          :libvirt__tunnel_port => "100#{2-i%2}",
          :libvirt__iface_name => "eth#{j}",
          auto_config: false
      end
      ((SP_number+SRV_per_leaf_pair+1)..22).each do |j|
        sw.vm.network :private_network,
          :libvirt__tunnel_type => "udp",
          :libvirt__tunnel_local_ip => "127.0.10.#{i}" ,
          :libvirt__tunnel_local_port => "100#{j}",
          :libvirt__tunnel_ip => "127.99.20.#{j}",
          :libvirt__tunnel_port => "9999",
          :libvirt__iface_name => "eth#{j}",
          auto_config: false
      end
      if (i%2 == 0) then 
	(23..24).each do |k|
	  sw.vm.network :private_network,
          :libvirt__tunnel_type => "udp",
          :libvirt__tunnel_local_ip => "127.0.20.#{i}" ,
          :libvirt__tunnel_local_port => "1100#{k}",
          :libvirt__tunnel_ip => "127.0.20.#{i-1}",
          :libvirt__tunnel_port => "1100#{k}",
          :libvirt__iface_name => "eth#{k}",
          auto_config: false
	end
      else 
	(23..24).each do |k|
          sw.vm.network :private_network,
          :libvirt__tunnel_type => "udp",
          :libvirt__tunnel_local_ip => "127.0.20.#{i}" ,
          :libvirt__tunnel_local_port => "1100#{k}",
          :libvirt__tunnel_ip => "127.0.20.#{i+1}",
          :libvirt__tunnel_port => "1100#{k}",
          :libvirt__iface_name => "eth#{k}",
          auto_config: false
        end
      end
    end
  end
  (1..(LF_number/2)).each do |i|
    (1..SRV_per_leaf_pair).each do |k|
      config.vm.define "client#{i}#{k}" do |cl|
        cl.ssh.username = "vagrant"
        cl.ssh.password = "vagrant"
        cl.vm.synced_folder ".", "/vagrant", disabled: true
        cl.vm.hostname =  "client#{i}#{k}"
        cl.vm.provider :libvirt do |spec|
          spec.nic_model_type = "e1000"
          end
        cl.vm.provision "shell", inline: <<-SHELL
             sudo yum install python3 -y
          SHELL
        cl.vm.box = "viniciusfs/centos7"
          (1..2).each do |l|
            cl.vm.network :private_network,
            :libvirt__tunnel_type => "udp",
            :libvirt__tunnel_local_ip => "127.0.30.#{i}#{k}",
            :libvirt__tunnel_local_port => "100#{l}",
	    :libvirt__tunnel_ip => "127.0.20.#{(2*i)+l-2}",
            :libvirt__tunnel_port => "100#{SP_number+k}",
            :libvirt__iface_name => "eth#{l}",
            auto_config: false
          end
      end
    end
  end 
  config.vm.define "oob-mgmt-server" do |oob|
    oob.ssh.username = "vagrant"
    oob.ssh.password = "vagrant"
    oob.vm.hostname = "oob-mgmt-server" 
    oob.vm.box = "viniciusfs/centos7"
    oob.vm.synced_folder "./share", "/vagrant", disabled: false
    oob.vm.hostname =  "oob.vm.name"
    oob.vm.provider :libvirt do |spec|
      spec.memory = 2048
      spec.nic_model_type = "e1000"
      end
    oob.vm.provision "shell", inline: <<-SHELL
          sudo yum install python3 -y
          sudo yum install epel-release -y
          sudo yum install ansible -y
          sudo pip3 install jinja2
          su - vagrant -c "ansible-galaxy collection install dellemc.enterprise_sonic"
       SHELL

  end
end
