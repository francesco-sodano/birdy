#!/usr/bin/env bash
# Project Birdy - v202110.1
# Copyright 2021 - Francesco Ares Sodano

apt-get update -y;
apt-get install git -y;
#create user birdy
#move to the home of birdy
mkdir -p $home/birdy;
birdyconf_var_run="/usr/lib/tmpfiles.d/birdy.conf";
if [ -e $birdyconf_var_run ]; then rm $birdyconf_var_run; fi
touch /usr/lib/tmpfiles.d/birdy.conf
echo "d /var/run/birdy 0775 birdy birdy -" > birdy.conf
echo "d /var/run/birdy/images 0775 birdy birdy -" >> birdy.conf