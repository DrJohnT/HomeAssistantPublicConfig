#!/bin/sh

# Invoke this script inside the HA docker instance using

# docker exec -it homeassistant bash ./nas710/install_ssh_keypair.sh

# copy the private key so it is accessible by root
mkdir -p /root/.ssh
cp /config/nas710/id* /root/.ssh/
cp /config/nas710/known_hosts /root/.ssh/
echo "Public/Private Keys Copied to /root/.ssh"

# Check if it is all working again
# ssh root@192.168.0.11 systemctl -help

# reset the flag by copying the HA_VERSION file
cp .HA_VERSION ./nas710/
echo "HA_VERSION Copied to nas710"





