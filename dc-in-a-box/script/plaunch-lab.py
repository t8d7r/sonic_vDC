import sys
import jinja2
from jinja2 import Template
LINE="============================================================================================"
nbspine=int(sys.argv[1])
nbleaf=int(sys.argv[2])
nbsrv=int(sys.argv[3])

print(LINE)
print('Generating Sonic.yaml  File')
vgf = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates/')).get_template('sonic.yaml.j2').render(nbspine=nbspine,nbleaf=nbleaf)
with open('./group_vars/sonic.yaml','w') as f: f.write(vgf)
print('sonic.yaml Generated:')
print (vgf)
print(LINE)
print('Generating leafs host var yaml  File')
for i in range(1,nbleaf*2+1):
    vgf = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates/')).get_template('leafs_common.yaml.j2').render(nbspine=nbspine,nbleaf=nbleaf,nbsrv=nbsrv,leafnumber=i)
    with open('./host_vars/leaf'+str(i)+'.yaml','w') as f: f.write(vgf)
    print('leaf '+str(i)+' host_var yaml Generated:')
    print (vgf)
    print(LINE)

print('Generating spines host var yaml  File')
for i in range(1,nbspine+1):
    vgf = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates/')).get_template('spines_common.yaml.j2').render(nbspine=nbspine,nbleaf=nbleaf,nbsrv=nbsrv,spinenumber=i)
    with open('./host_vars/spine'+str(i)+'.yaml','w') as f: f.write(vgf)
    print('spine '+str(i)+' host_var yaml Generated:')
    print (vgf)
    print(LINE)

print('Generating client  host var yaml  File')
for i in range(1,nbleaf+1):
    for j in range(1,nbsrv+1):
        vgf = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates/')).get_template('clients_common.yaml.j2').render(i=i,j=j)
        with open('./host_vars/client'+str(i)+str(j)+'.yaml','w') as f: f.write(vgf)
        print('client'+str(i)+str(j)+'yaml Generated:')
        print (vgf)
print(LINE)

print('Generating topology.yaml  File')
vgf = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates/')).get_template('topology.yaml.j2').render(nbspine=nbspine,nbleaf=nbleaf,nbsrv=nbsrv)
with open('./topology','w') as f: f.write(vgf)
print('Topology Generated:')
print (vgf)
print(LINE)
