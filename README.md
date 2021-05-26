# sonic_vDC
# Interactive Vagrant for SONiC Lab Environment
Tested with:
   * Ubuntu 20.04.1 LTS
   * ansible 2.9.6
   * python 3.8.5 
   * vagrant 2.2.16
      * *VER="2.2.16" ; wget https://releases.hashicorp.com/vagrant/${VER}/vagrant_${VER}_x86_64.deb ; sudo dpkg -i vagrant_${VER}_x86_64.deb*

## Step by step procedure to set up the environment: 
1. Clone the project
   * *git clone https://github.com/t8d7r/sonic_vDC*
2. Add the vagrant SONiC box.
   * *vagrant box add --name sonic-d SONiC.box*
3. Run vagrant up and define number of spines (between 1 and 4), number of leaf pair (between 1 and 4) and number of server per leaf pair (between 1 and 4):
   * If only the physical topology is required without provisioning the configs use:
       * *vagrant up --no-provision*

## Tips 
1. Several files are generated automatically :
   * topology with addressing details of switches & hosts
   * inventory for ansible
   * hosts_vars
2. A new environment can be generated after destroying all vms 
   * *vagrant destroy -f* or *vagrant destroy vm_name* on each vm
3. Pair server are part of L2 vni , odd client servers are part of L3 VNI with symmetric IRB
4. Native vagrant ansible provisionner is not used, instead a mgmt vm is used to run ansible playbook, it is based on DellEMC SONiC collection : https://github.com/ansible-collections/dellemc.enterprise_sonic

