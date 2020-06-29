import markdown
from bs4 import BeautifulSoup
import json
import os




def create_manifests(ver, path):
    print("Creating manifests...")

    os.mkdir(path) if not os.path.isdir(path) else None

    client_manifest = {}
    server_manifest = {}

    client_manifest['minecraft'] = ver
    server_manifest['minecraft'] = ver

    client_manifest['mods'] = []
    server_manifest['mods'] = []

    html = markdown.markdown(open("README.md").read(), extensions=['tables'])
    soup = BeautifulSoup(html, 'html.parser')

    rows = soup.find("table").find("tbody").find_all("tr")

    for row in rows:
        cells = row.find_all("td")
        
        mod_name = cells[0].get_text()
        mod_id = cells[1].get_text()
        mod_type = cells[3].get_text()

        if mod_type == "C":
            # add to client manifest
            client_manifest['mods'].append({
                'name': mod_name,
                'id': mod_id,
                'type': mod_type
            })
        elif mod_type == "S":
            # add to server manifest
            server_manifest['mods'].append({
                'name': mod_name,
                'id': mod_id,
                'type': mod_type
            })
        else:
            # add to both client and server manifest
            client_manifest['mods'].append({
                'name': mod_name,
                'id': mod_id,
                'type': mod_type
            })

            server_manifest['mods'].append({
                'name': mod_name,
                'id': mod_id,
                'type': mod_type
            })      

    
    with open(path+'client_manifest.json', 'w') as outfile:
        json.dump(client_manifest, outfile, indent=4)
    
    with open(path+'server_manifest.json', 'w') as outfile:
        json.dump(server_manifest, outfile, indent=4)
    
    print("Done manifests.")


if __name__ == "__main__":
    print("Nothing to do.")
    pass

        