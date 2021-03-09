#!/bin/bash
#T8d7r
LINE="============================================================================================"
clear
choice=0
nbspine=0
nb_srv=0
nb_leaf=0
echo -e "\n$LINE"
echo "		Set spine number (between 1 and 4)		"
read -p "Spines number : " choice
while [[ !("$choice" =~ ^[0-9]+$) ]] 
do
  echo -e "\n=> Enter a number between 1 and 4 <="
  read -p "Spines number : " choice
done
if [ "$choice" -ge 1 -a "$choice" -le 4 ]; then
	nbspine=$choice
else 
	while [ "$choice" -lt 1 -o "$choice" -gt 4 ]
	do
        	echo -e "\n=> Enter a number between 1 and 4 <="
        	read -p "Spines number : " choice
        	if [ "$choice" -ge 1 -o "$choice" -le 4 ]; then
                	nbspine=$choice
                	echo -e "\n $choice"
        	else
                	echo -e "Enter a spine number between 1 and 4"
        	fi
	done
fi
echo -e "\n$LINE"
echo -e "\n$nbspine"
echo -e "\n$LINE"
