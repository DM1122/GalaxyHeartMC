#!/bin/bash
# shutdown-script-url: gs://mc-staging-bucket/cloud/boot/shutdown.sh

# stop server
sudo screen -r mcs -X stuff '/stop\n'

cd ~

# backup data
sudo gsutil rsync -d -r /home/server/world gs://mc-staging-bucket/world
sudo gsutil rsync -d -r /home/server/logs gs://mc-staging-bucket/logs
sudo gsutil rsync -d -r /home/server/crash-reports gs://mc-staging-bucket/crash-reports
