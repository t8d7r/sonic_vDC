# sonic_vDC
# Interactive Vagrant for SONiC Lab Environment
This work is inspired by incredible teammate work made on OS10 which can be found here : https://github.com/Doods111/DELLOS10 & other lessons learnt from DellEMC experts

Tested with:
   * Ubuntu 20.04.1 LTS
   * ansible 2.9.6
   * python 3.8.5 
   * vagrant 2.2.16
      * *VER="2.2.16" ; wget https://releases.hashicorp.com/vagrant/${VER}/vagrant_${VER}_x86_64.deb ; sudo dpkg -i vagrant_${VER}_x86_64.deb*

## Step by step procedure to set up the environment: 
1. Install vagrant :
   * *sudo apt install -y qemu qemu-kvm libvirt-daemon-system libvirt-clients libxslt-dev libxml2-dev libvirt-dev zlib1g-dev ruby-dev ruby-libvirt ebtables dnsmasq-base  bridge-utils  virt-manager build-essential nfs-kernel-server*
   * *VER="2.2.16" ; wget https://releases.hashicorp.com/vagrant/${VER}/vagrant_${VER}_x86_64.deb ; sudo dpkg -i vagrant_${VER}_x86_64.deb*
   * *vagrant plugin install vagrant-libvirt; vagrant plugin install vagrant-hostmanager; vagrant plugin install vagrant-sshfs*
   * *sudo systemctl restart libvirtd*
2. Clone the project
   * *git clone https://github.com/t8d7r/sonic_vDC*
4. Add the vagrant SONiC box.
   * *vagrant box add --name sonic-d SONiC.box*
5. Run vagrant up and answer interactive question to define number of spines (between 1 and 4), number of leaf pair or racks (between 1 and 4) and number of server per leaf pair (between 1 and 4):
   * If only the physical topology is required without provisioning the configs use:
       * *vagrant up --no-provision*

## Tips 
1. Pay attention to ressource consumption, for instance Ubuntu VM specs to run a 2 spines, 2 pairs of leaves and 2 server clients per leaf pair is 4 vCPU, 32Go RAM and 256Go storage 
2. Several files are generated automatically :
   * topology with addressing details of switches & hosts
   * inventory for ansible
   * hosts_vars
3. A new environment can be generated after destroying all vms 
   * *vagrant destroy -f* or *vagrant destroy vm_name* on each vm
4. Pair server are part of L2 vni , odd client servers are part of L3 VNI with symmetric IRB
5. Native vagrant ansible provisionner is not used, instead a mgmt vm is used to run ansible playbook, playbook use DellEMC SONiC collection : https://github.com/ansible-collections/dellemc.enterprise_sonic

