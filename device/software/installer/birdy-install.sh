#!/usr/bin/env bash
# Project Birdy - v202110.1
# Copyright 2021 - Francesco Ares Sodano
curl https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb > ./packages-microsoft-prod.deb;
sudo apt install ./packages-microsoft-prod.deb;
apt-get update -y;
apt-get install git -y;
sudo apt-get install moby-engine -y;
#create user birdy
sudo adduser birdy
sudo usermod -a -G adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,gpio,i2c,spi birdy
sudo usermod -a -G docker birdy
#configure git
# git config --global user.email "francesco-sodano@github.com"
# git config --global user.name "francesco-sodano"
#move to the home of birdy
mkdir -p $home/birdy;
birdyconf_var_run="/usr/lib/tmpfiles.d/birdy.conf";
if [ -e $birdyconf_var_run ]; then rm $birdyconf_var_run; fi
touch /usr/lib/tmpfiles.d/birdy.conf
echo "d /var/run/birdy 0775 birdy birdy -" > birdy.conf
echo "d /var/run/birdy/images 0775 birdy birdy -" >> birdy.conf