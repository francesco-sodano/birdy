#!/usr/bin/env bash
# Project Birdy - v20220910.1
# Copyright 2022 - Francesco Ares Sodano

# Add Microsoft Repository
curl https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb > ./packages-microsoft-prod.deb;
apt install ./packages-microsoft-prod.deb;

# Add Google Package Repository (TensorFlow)
echo "deb [signed-by=/usr/share/keyrings/coral-edgetpu-archive-keyring.gpg] https://packages.cloud.google.com/apt coral-edgetpu-stable main" | tee /etc/apt/sources.list.d/coral-edgetpu.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | tee /usr/share/keyrings/coral-edgetpu-archive-keyring.gpg >/dev/null

# Install required packages
apt-get update -y;
apt-get install -y --no-install-recommends \
    git \
    libatlas-base-dev=3.10.3-10+rpi1 \
    python3=3.9.2-3 \
    python3-pip=20.3.4-4+rpt1+deb11u1 \
    python3-gpiozero=1.6.2-1 \
    python3-tflite-runtime=2.5.0.post1 \
    python3-picamera2=0.3.3-1;

pip3 install opencv-python==4.6.0.66

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh ./get-docker.sh
usermod -aG docker birdy

# Configure git
git config --global user.email "birdy@github.com"
git config --global user.name "birdy"

# Create directory and clean up
mkdir ~/projects;
rm ./packages-microsoft-prod.deb
rm ./get-docker.sh

# Disable Camera logs
export LIBCAMERA_LOG_LEVELS=*:4