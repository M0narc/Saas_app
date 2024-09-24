import requests
from pathlib import Path

def download_to_local(url:str, 
                      destination_path:Path, 
                      parent_mkdir:bool=True):
    if not isinstance(destination_path, Path):
        raise ValueError(f"{destination_path} must be a valid pathlib path object")
    if parent_mkdir:
        destination_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Write the file out in binary mode to prevent any new 
        # line conversion
        destination_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f'Failed to download {url}: {e}')
        return False
