#!/bin/bash
# startup-script-url: gs://mc-staging-bucket/boot/startup.sh

# update instance
apt-get update
apt-get upgrade

# install dependencoes
apt-get install -y default-jre-headless
apt-get install -y screen

# clear outdated server content
rm -rf /home/*      
cd /home

# copy server and world from bucket
gsutil cp -r gs://mc-staging-bucket/server .
gsutil cp -r gs://mc-staging-bucket/world server

# start server
screen -d -m -S mcs java -Xms1G -Xmx3G -jar forge.jar nogui