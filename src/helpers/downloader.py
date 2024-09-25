import logging
import requests
from pathlib import Path

logging.basicConfig(level=logging.INFO)

def download_to_local(url:str, 
                      destination_path:Path, 
                      parent_mkdir:bool=True,
                      overwrite: bool = False,
                      timeout: int = 10) -> bool:
    
    if not isinstance(destination_path, Path):
        raise ValueError(f"{destination_path} must be a valid pathlib path object")
    
    if parent_mkdir:
        destination_path.parent.mkdir(parents=True, exist_ok=True)

    if destination_path.exists() and not overwrite:
        logging.info(f"File already exists: {destination_path}. skipping download")
        return True

    try:
        logging.info(f"Downloading {url} to {destination_path}")
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        # Write the file out in binary mode to prevent any new 
        # line conversion
        destination_path.write_bytes(response.content)
        logging.info(f"Successfully downloaded {url}")
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download {url}: {e}")
        return False
