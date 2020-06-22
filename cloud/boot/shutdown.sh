#!/bin/bash
# shutdown-script-url: gs://mc-staging-bucket/cloud/boot/shutdown.sh

cd ~

# stop server
sudo screen -r mcs -X stuff '/stop\n'

# backup data
sudo gsutil rsync -d -r /home/server/world gs://mc-staging-bucket/world
sudo gsutil rsync -d -r /home/server/logs gs://mc-staging-bucket/logs
sudo mkdir -p /home/server/crash-reports
sudo gsutil rsync -d -r /home/server/crash-reports gs://mc-staging-bucket/crash-reports
