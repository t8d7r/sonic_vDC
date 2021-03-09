import jinja2
from jinja2 import Template
LINE="============================================================================================"
choice=0
nbspine=0
nbsrv=0
nbleaf=0
print(LINE)
while ((nbspine < 1) or (nbspine > 4)): 
    try:
        nbspine = int(input("Please enter spine number:\n"))
    except ValueError:
        print("Input was not a number, please enter a number between 1 and 4")
    if ((nbspine < 1) or (nbspine > 4)):
        print("Please enter a number between 1 and 4")

while ((nbleaf < 1) or (nbleaf > 4)):
    try:
        nbleaf = int(input("Please enter leaf pair number:\n"))
    except ValueError:
        print("Input was not a number, please enter a leaf pair number between 1 and 4")
    if ((nbleaf < 1) or (nbleaf > 4)):
        print("Please enter a number between 1 and 4")

while ((nbsrv < 1) or (nbsrv > 4)):
    try:
        nbsrv = int(input("Please enter srv per leaf number :\n"))
    except ValueError:
        print("Input was not a number, please enter a srv per leaf number between 1 and 4")
    if ((nbsrv < 1) or (nbsrv > 4)):
        print("Please enter a number between 1 and 4")

print('Spine number = ',nbspine)
print('Leaf pair number = ',nbleaf)
print('Srv per leaf number = ',nbsrv)

print(LINE)
print('Generating Inventory')
inv = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates/')).get_template('inventory.j2').render(nbspine=nbspine,nbleaf=nbleaf,nbsrv=nbsrv)
with open('testinventory','w') as f: f.write(inv)
print('Inventory Generated:')
print (inv)
print(LINE)
print('Generating Vagrant File')
vgf = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates/')).get_template('Vagrantfile.j2').render(nbspine=nbspine,nbleaf=nbleaf,nbsrv=nbsrv)
with open('testVagrantfile','w') as f: f.write(vgf)
print('Vagrantfile Generated:')
print (vgf)
print(LINE)
