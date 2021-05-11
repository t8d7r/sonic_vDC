# sonic_vDC
# Interactive Vagrant for SONiC Lab Environment
Tested with:
   * Ubuntu 20.04.1 LTS
   * ansible 2.9.6
   * python 3.8.5 
   * vagrant 2.2.6
      * *VER="2.2.6" ; wget https://releases.hashicorp.com/vagrant/${VER}/vagrant_${VER}_x86_64.deb ; sudo dpkg -i vagrant_${VER}_x86_64.deb*

## Step by step procedure to set up the environment: 
1. Clone the project
   * *git clone https://github.com/t8d7r/sonic_vDC* *
2. Add the vagrant SONiC box.
   * *vagrant box add --name SONiC .box*
3. Run vagrant up and define number of spines, number of leaf pair and number of server per leaf pair :
   * If only the physical topology is required without provisioning the configs use:
       * *vagrant up --no-provision*
