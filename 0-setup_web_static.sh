#!/usr/bin/env bash
#Script to set up web servers for deployment

#Install nginx if not installed
sudo apt-get update
sudo apt-get install nginx -y


mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/current

"Simple content to test Nginx configuration" > /data/web_static/releases/test/index.html

if test -L /data/web_static/current; then
	rm /data/web_static/current
	fi
ln -s /data/web_static/current /data/web_static/releases/test/

sudo chown -R "ubuntu:ubuntu" /data

detail="alais \/data\/web_static\/current\/;\n\n\tautoindex off;\n}\n"
location="}\n\nlocation /hbnb_static {\n\n\t$detail"
sed -i "1,/}/ s|}|$location|" /etc/nginx/sites-available/default"
sudo nginx service restart
