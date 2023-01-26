#!/usr/bin/env bash
#Script to set up web servers for deployment

#Install nginx if not installed
sudo apt-get update
sudo apt-get install nginx -y

#Firewall
sudo ufw allow 'Nginx HTTP'


[ ! -d /data/web_static/shared/ ] && mkdir -p /data/web_static/shared/
[ ! -d /data/web_static/releases/test/ ] && mkdir -p /data/web_static/releases/test/

echo "Simple content to test Nginx configuration" > /data/web_static/releases/test/index.html

[ -f /data/web_static/current ] && sudo rm /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R "ubuntu:ubuntu" /data/


detail="alais \/data\/web_static\/current\/;\n\t}\n"
location="\n\tlocation \/hbnb_static {\n\n\t$detail"
sed -i "37s/$/$location/" /etc/nginx/sites-available/default

sudo service nginx restart
