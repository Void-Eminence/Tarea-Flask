#!/bin/bash
if [ "$EUID" -ne 0 ]; then
   echo "Este script requiere permisos de root."
   exit
fi


apt-get update
apt-get install -y python3-pip

git clone https://dev.ilab.cl/public/pythonweb.git /srv

cd /srv
pip3 install setuptools gunicorn
pip3 install -r web-interface/requirements.txt

cp -f webinterface.service.sample /etc/systemd/system/webinterface.service

systemctl unmask webinterface.service
systemctl enable webinterface.service
systemctl start webinterface.service
