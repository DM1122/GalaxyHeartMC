import os
import requests as rq
import json
import sys
from datetime import datetime
from progress.bar import Bar



def get_mod_name(idd):
    data = json.loads(rq.get(f"https://curse.nikky.moe/api/addon/{idd}").content)
    name = data["name"]

    return name    


def download_mod(idd, ver, path):
    # Get mod's latest version for this game version
    data = json.loads(rq.get(f"https://curse.nikky.moe/api/addon/{idd}/files").content)

    # Get the latest mod version which supports the game version
    candidates = [candidate for candidate in data if ver in candidate["gameVersion"]]
    release_dates = [datetime.strptime(candidate["fileDate"], "%Y-%m-%dT%H:%M:%S") for candidate in candidates]

    zipped_lists = zip(release_dates, candidates)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    release_dates_ord, candidates_ord = [list(tuple) for tuple in  tuples]
    ver_latest = candidates_ord[-1]

    # Download the mod
    if os.path.isfile(path + ver_latest["fileName"]): # Don't redownload mods we may already have downloaded
        print(f"Mod '{get_mod_name(idd)}' (ID: {idd}) already downloaded! Skipping.")
    else:
            download = rq.get(ver_latest["downloadUrl"])
            assert download.status_code == 200 # Make sure we're good
            with open(path + ver_latest["fileName"], "wb") as f:
                f.write(download.content)


def get_mods_from_manifest(manifest_path, download_path):
    print(f"Getting mods listed in '{manifest_path}'...")


    os.makedirs(download_path) if not os.path.isdir(download_path) else None
    
    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    VERSION = manifest["minecraft"]
    idds = [mod['id'] for mod in manifest['mods']]

    with Bar('Starting downloads', max=len(idds)) as bar:
        for idd in idds:
            bar.message = f"Downloading '{get_mod_name(idd)}'"
            download_mod(idd=idd, ver=VERSION, path=download_path)
            bar.next()
            
    print("Mod downloads complete!")


if __name__ == "__main__":
    pass






