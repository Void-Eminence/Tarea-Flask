#!/bin/bash

if [ "$EUID" -ne 0 ]; then 
   echo "Este script requiere permisos de root."
   exit
fi


apt update
apt install -y python3-pip 

pip3 install --break-system-packages  setuptools gunicorn
pip3 install --break-system-packages -r web-interface/requirements.txt
