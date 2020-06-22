#!/bin/bash
# shutdown-script-url: gs://mc-staging-bucket/boot/shutdown.sh

# stop server
sudo screen -r mcs -X stuff '/stop\n'

# backup data
cd /home
gsutil cp -r server/world gs://mc-staging-bucket
gsutil cp -r server/logs gs://mc-staging-bucket
gsutil cp -r server/crash-reports gs://mc-staging-bucket
