#!/bin/sh

# NOTE: this script can now be run from home assistant

# Invoke this script inside the homeassistant docker instance using

# docker exec -it homeassistant bash ./nas710/install_ssh_keypair.sh

# copy the private key so it is accessible by root
mkdir -p /root/.ssh
cp /config/nas710/id* /root/.ssh/
cp /config/nas710/known_hosts /root/.ssh/
chmod 400 /root/.ssh/id_rsa
echo "Public/Private Keys Copied to /root/.ssh"

# Check if it is all working again
# ssh root@192.168.0.47 systemctl -help

# reset the flag by copying the HA_VERSION file
cp .HA_VERSION ./nas710/
echo "HA_VERSION Copied to nas710"





