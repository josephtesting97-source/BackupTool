import os
import hashlib
import json
import requests

UPLOAD_URL = "https://chug-frostbite-outthink.ngrok-free.dev/upload"
HASH_FILE = ".filehashes.json"

# Load previous hashes
if os.path.exists(HASH_FILE):
    with open(HASH_FILE, "r") as f:
        saved_hashes = json.load(f)
else:
    saved_hashes = {}

def get_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def upload_file(filepath):
    with open(filepath, "rb") as f:
        files = {"file": (os.path.basename(filepath), f)}
        response = requests.post(UPLOAD_URL, files=files)
        print(f"Upload {filepath}: {response.status_code}")
        try:
            print(response.json())
        except:
            print(response.text)

def main():
    current_hashes = {}

    for filename in os.listdir("."):
        if not os.path.isfile(filename):
            continue

        # skip the hash file itself
        if filename == HASH_FILE:
            continue

        file_hash = get_file_hash(filename)
        current_hashes[filename] = file_hash

        # Check if new or modified
        if filename not in saved_hashes:
            print(f"[NEW] {filename}")
            upload_file(filename)

        elif saved_hashes[filename] != file_hash:
            print(f"[MODIFIED] {filename}")
            upload_file(filename)

        else:
            print(f"[UNCHANGED] {filename}")

    # Save updated hashes
    with open(HASH_FILE, "w") as f:
        json.dump(current_hashes, f, indent=2)

if __name__ == "__main__":
    main()
