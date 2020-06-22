from googleapiclient import discovery

project = 'minecraft-280820'
zone = 'us-east1-b'
instance = 'mc-server-1'

def stop_server(req):
    print('Sending server shutdown command...')

    service = discovery.build('compute', 'v1')
    request = service.instances().stop(project=project, zone=zone, instance=instance)
    response = request.execute()

    print(response)

    return f"The server shutdown command has been sent."