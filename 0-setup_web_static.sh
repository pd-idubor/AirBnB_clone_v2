#!/usr/bin/env bash
#Script to set up web servers for deployment

sudo apt-get update -y
[ ! -f /usr/sbin/nginx ] && sudo apt-get install nginx -y

#Firewall
sudo ufw allow 'Nginx HTTP'

[ ! -d /data/web_static/releases/test/ ] && sudo mkdir -p /data/web_static/releases/test/
[ ! -d /data/web_static/shared/ ] && sudo mkdir -p /data/web_static/shared/

echo "<!DOCTYPE html>
<html>
	<head>
	</head>
	<body>
		<p>Configuration test<p>
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html


[ -f /data/web_static/current ] && sudo rm /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R "ubuntu:ubuntu" /data/

detail="alias \/data\/web\_static\/current\/;"
location="\n\tlocation \/hbnb\_static\/ {\n\t\t$detail\n\t}\n"
sed -i "37s/$/$location/" /etc/nginx/sites-available/default

sudo service nginx restart
