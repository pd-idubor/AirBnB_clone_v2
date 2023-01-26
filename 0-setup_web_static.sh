#!/usr/bin/env bash
#Script to set up web servers for deployment

#Install nginx if not installed
sudo apt-get update
[ ! -f /usr/sbin/nginx ] && sudo apt-get install -y nginx

#Firewall
sudo ufw allow 'Nginx HTTP'


[ ! -d /data/web_static/shared/ ] && mkdir -p /data/web_static/shared/
[ ! -d /data/web_static/releases/test/ ] && mkdir -p /data/web_static/releases/test/

echo "Simple content to test Nginx configuration" > /data/web_static/releases/test/index.html

[ -f /data/web_static/current ] && sudo rm /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R "ubuntu:ubuntu" /data/


detail="alais \/data\/web\_static\/current\/;\n\t}\n"
location="\n\tlocation \/hbnb\_static\/ {\n\t\t$detail"
sed -i "37s/$/$location/" /etc/nginx/sites-available/default

sudo service nginx restart
