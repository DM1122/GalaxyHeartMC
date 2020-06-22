#!/bin/bash
# startup-script-url: gs://mc-staging-bucket/cloud/boot/startup.sh

sudo su
cd ~

# update instance
apt-get update
# apt-get upgrade (needs prompt?)

# install dependencies
apt-get install -y default-jre-headless
apt-get install -y screen

# copy server and world from bucket
gsutil rsync -d -r gs://mc-staging-bucket/server /home/server
gsutil rsync -d -r gs://mc-staging-bucket/world /home/server/world

# start server
cd /home/server
screen -d -m -S mcs java -Xms1G -Xmx3G -jar forge.jar nogui