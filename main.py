import requests
import os
import zipfile
import subprocess
import shutil

# Replace with the owner and repo of the extension
OWNER = "VampireChicken12"
REPO = "youtube-enhancer"

response = requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest")
response.raise_for_status()

latest_version = response.json()["tag_name"]

# Check if the latest version is already downloaded
try:
    with open("latest_version.txt", "r") as f:
        downloaded_version = f.read().strip()
except FileNotFoundError:
    downloaded_version = None

if latest_version != downloaded_version:
    # Extract the download URL for the Chrome release asset
    assets = response.json()["assets"]
    chrome_asset = next(asset for asset in assets if "Chrome" in asset["name"])
    asset_url = chrome_asset["browser_download_url"]

    # Download the release asset
    asset_response = requests.get(asset_url)
    asset_response.raise_for_status()

    with open("extension.zip", "wb") as f:
        f.write(asset_response.content)

    extension_path = r"C:\Users\admin\Downloads\chrome-extension-from-github\extension"

    if os.path.exists(extension_path):
        shutil.rmtree(extension_path)

    with zipfile.ZipFile("extension.zip", "r") as zip_ref:
        zip_ref.extractall(extension_path)

    # Save the version number of the downloaded release
    with open("latest_version.txt", "w") as f:
        f.write(latest_version)
