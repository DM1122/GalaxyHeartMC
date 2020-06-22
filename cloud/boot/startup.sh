#!/bin/bash
# startup-script-url: gs://mc-staging-bucket/cloud/boot/startup.sh

cd ~

# update instance
sudo apt-get update && sudo apt-get -y upgrade

# install dependencies
sudo apt-get install -y default-jre-headless
sudo apt-get install -y screen
sudo apt-get install -y htop

# copy server and world from bucket
sudo mkdir -p /home/server
sudo gsutil rsync -d -r gs://mc-staging-bucket/server /home/server
sudo mkdir -p /home/server/world
sudo gsutil rsync -d -r gs://mc-staging-bucket/world /home/server/world

# start server
cd /home/server
sudo screen -d -m -S mcs java -Xms1G -Xmx6G -jar forge.jar nogui