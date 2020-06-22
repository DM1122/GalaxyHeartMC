from googleapiclient import discovery

project = 'minecraft-280820'
zone = 'us-east1-b'
instance = 'mc-server-1'

def start_server(req):
    print('Sending server startup command...')

    service = discovery.build('compute', 'v1')
    request = service.instances().start(project=project, zone=zone, instance=instance)
    response = request.execute()

    print(response)

    return f"The server startup command has been sent."
