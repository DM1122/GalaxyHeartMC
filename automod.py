from libs import manifester, modownloader

game_ver = "1.15.2"
manifest_path = "manifests/"
mods_client_path = "mods/client/"
mods_server_path = "mods/server/"

if __name__ == "__main__":
    print("Auto-updating mods...")
    manifester.create_manifests(ver=game_ver, path=manifest_path)

    # modownloader.get_mods_from_manifest(manifest_path=manifest_path+"client_manifest.json", download_path=mods_client_path)
    modownloader.get_mods_from_manifest(manifest_path=manifest_path+"server_manifest.json", download_path=mods_server_path)



