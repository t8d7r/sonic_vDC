# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

if Dir.exist?("./.vagrant/machines")
  sp_number = `ls .vagrant/machines/ | grep spine | wc -l`.to_i
  lf_number = `ls .vagrant/machines/ | grep leaf | wc -l`.to_i
  oob_number = `ls .vagrant/machines/ | grep oob | wc -l`.to_i
  if lf_number != 0
    srv_per_leaf_pair = `ls .vagrant/machines/ | grep client | wc -l`.to_i/(lf_number/2)
  else
    srv_per_leaf_pair = 0
  end
else
  sp_number = 0
  lf_number = 0
  srv_per_leaf_pair = 0
  oob_number = 0
end

if ARGV[0] == "up" && (ARGV.length == 1 or ARGV[1] == "--no-provision") && !(Dir.exist?("./.vagrant/machines"))
  nbspine=0
  nbsrv=0
  nbleaf=0
  LINE="============================================================================================"
  while ((nbspine < 1) or (nbspine > 4))
    print("Please enter a spine number between 1 and 4\n")
    nbspine = STDIN.gets.chomp.to_i
  end
  while ((nbleaf < 1) or (nbleaf > 4))
    print("Please enter a leaf pair number between 1 and 4\n")
    nbleaf = STDIN.gets.chomp.to_i
  end
  while ((nbsrv < 1) or (nbsrv > 4))
    print("Please enter a server per leaf number between 1 and 4\n")
    nbsrv = STDIN.gets.chomp.to_i
  end
  puts ("#{LINE}\n\n")
  puts ("Nombre de spines : #{nbspine}\n")
  puts ("Nombre de paire de leaf : #{nbleaf}\n")
  puts ("Nombre de serveurs par leaf : #{nbsrv}\n\n")
  puts ("#{LINE}\n")

  system("python3 ./script/plaunch-lab.py #{nbspine} #{nbleaf} #{nbsrv}")

  sp_number = nbspine
  lf_number = 2*nbleaf
  srv_per_leaf_pair = nbsrv
  oob_number = 1
end

Vagrant.configure("2") do |config|
  config.ssh.username = "admin"
  config.ssh.password = "YourPaSsWoRd"
  (1..sp_number).each do |i|
    config.vm.define "spine#{i}" do |sw|
      sw.vm.synced_folder ".", "/vagrant", disabled: true
      sw.vm.box = "sonic-d"
      (1..lf_number).each do |j|
        sw.vm.network :private_network,
	  :libvirt__tunnel_type => "udp",
	  :libvirt__tunnel_local_ip => "127.0.10.#{i}" ,
	  :libvirt__tunnel_local_port => "100#{j}",
	  :libvirt__tunnel_ip => "127.0.20.#{j}",
          :libvirt__tunnel_port => "100#{i}",
	  :libvirt__iface_name => "eth#{j}",
          :mac => "52:54:00:75:0#{i}:#{j+10}",
          auto_config: false
        end
      ((lf_number+1)..24).each do |j|
        sw.vm.network :private_network,
          :libvirt__tunnel_type => "udp",
          :libvirt__tunnel_local_ip => "127.0.10.#{i}" ,
          :libvirt__tunnel_local_port => "100#{j}",
          :libvirt__tunnel_ip => "127.99.20.#{j}",
          :libvirt__tunnel_port => "9999",
          :libvirt__iface_name => "eth#{j}",
          :mac => "52:54:00:75:0#{i}:#{j+10}",
	auto_config: false
        end
    end
  end
  (1..lf_number).each do |i|
    config.vm.define "leaf#{i}" do |sw|
      sw.vm.synced_folder ".", "/vagrant", disabled: true
      sw.vm.box = "sonic-d"
      (1..sp_number).each do |j|
        sw.vm.network :private_network,
          :libvirt__tunnel_type => "udp",
          :libvirt__tunnel_local_ip => "127.0.20.#{i}" ,
          :libvirt__tunnel_local_port => "100#{j}",
          :libvirt__tunnel_ip => "127.0.10.#{j}",
          :libvirt__tunnel_port => "100#{i}",
          :libvirt__iface_name => "eth#{j}",
          :mac => "52:54:00:75:A#{i}:#{j+10}",
          auto_config: false
      end
      (sp_number+1..sp_number+srv_per_leaf_pair).each do |j|
        sw.vm.network :private_network,
          :libvirt__tunnel_type => "udp",
          :libvirt__tunnel_local_ip => "127.0.20.#{i}" ,
          :libvirt__tunnel_local_port => "100#{j}",
          :libvirt__tunnel_ip => "127.0.30.#{(i+(i%2))/2}#{j-sp_number}",
          :libvirt__tunnel_port => "100#{2-i%2}",
          :libvirt__iface_name => "eth#{j}",
          :mac => "52:54:00:75:A#{i}:#{j+10}",
          auto_config: false
      end
      ((sp_number+srv_per_leaf_pair+1)..22).each do |j|
        sw.vm.network :private_network,
          :libvirt__tunnel_type => "udp",
          :libvirt__tunnel_local_ip => "127.0.10.#{i}" ,
          :libvirt__tunnel_local_port => "100#{j}",
          :libvirt__tunnel_ip => "127.99.20.#{j}",
          :libvirt__tunnel_port => "9999",
          :libvirt__iface_name => "eth#{j}",
          :mac => "52:54:00:75:A#{i}:#{j+10}",
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
          :mac => "52:54:00:75:A#{i}:#{k+10}",
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
          :mac => "52:54:00:75:A#{i}:#{k+10}",
          auto_config: false
        end
      end
    end
  end
  (1..(lf_number/2)).each do |i|
    (1..srv_per_leaf_pair).each do |k|
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
            :libvirt__tunnel_port => "100#{sp_number+k}",
            :libvirt__iface_name => "eth#{l}",
            :mac => "52:54:00:75:#{i}#{k}:0#{l}",
            auto_config: false
          end
      end
    end
  end 
  if (oob_number == 1)
    config.vm.define "oob-mgmt-server" do |oob|
      oob.ssh.username = "vagrant"
      oob.ssh.password = "vagrant"
      oob.vm.hostname = "oob-mgmt-server" 
      oob.vm.box = "viniciusfs/centos7"
      oob.vm.synced_folder "./", "/vagrant", disabled: false , type: "nfs"
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
  config.trigger.after :up do |trigger|
    trigger.name = "Generate inventory"
    trigger.only_on = "oob-mgmt-server"
    trigger.run = {inline: "bash -c 'for line in $(vagrant status | cut -f 1 -d \" \" | head -n -4 | tail -n +3) ; do echo $line\" ansible_host=\"\"$(vagrant ssh-config $line| head -n 2 | tail -n 1 | cut -f 4 -d \" \")\" ; done > inventory && echo \"[spines]\" >> inventory && for i in {1..#{sp_number}} ; do echo \"spine\"$i ; done >> inventory && echo \"[leafs]\" >> inventory && for i in {1..#{lf_number}} ; do echo \"leaf\"$i ; done >> inventory && echo \"[clients]\" >> inventory && for i in {1..#{lf_number/2}} ; do for j in {1..#{srv_per_leaf_pair}} ; do echo \"client\"$i$j ; done ; done >> inventory && echo \"[mgmtserver]\" >> inventory && echo \"oob-mgmt-server\"  >> inventory && echo \"[sonic:children]\nspines\nleafs\" >> inventory '"}
  end
  config.trigger.after :up do |trigger|
    trigger.name = "Infra deployment with ansible playbook"
    trigger.only_on = "oob-mgmt-server"
    if ((ARGV[ARGV.length - 1] != "--no-provision") )
      trigger.run_remote = {inline: "export ANSIBLE_CONFIG=/vagrant/ansible.cfg && ansible-playbook /vagrant/deploy.yaml"}
    end
  end
 
  config.trigger.after :destroy do |trigger|
    trigger.name = "Clean file after destroy"
    trigger.ruby do |env,machine|
      if ((ARGV[1] == "-f" && Dir.exist?("./.vagrant/machines/")) or Dir.empty?("./.vagrant/machines/")) && File.exist?("./host_vars/#{machine.name}.yaml")
        system ("rm ./host_vars/#{machine.name}.yaml" )
      end
      if Dir.empty?("./host_vars")
        if Dir.exist?("./.vagrant/machines")
          system ("rm -rf ./.vagrant/machines")
        end 
        if File.exist?("./inventory")
          system ("rm ./inventory")
        end
        if File.exist?("./topology")
          system ("rm ./topology")
        end
      end
    end
  end
end
