yeah so i want to get latest extension releases but it's not on chrome webstore so i asked Bing and it helped me write this. most stuff is ai gen so yeah.

the following readme was also written by Bing AI

you can run the script periodically to get latest release or just add it to task scheduler or some shit

# Auto-Update Chrome Extension from GitHub Releases

This Python script allows you to automatically download the latest release of a Chrome extension from GitHub and extract it to a specified directory. This can be useful if the extension is not available on the Chrome Web Store or if you want to use the latest version from GitHub.

## Prerequisites

- Python 3
- `requests` library in Python

You can install `requests` using pip:

```bash
pip install requests
```

## Usage

1. Replace `OWNER` and `REPO` in the script with the GitHub username and repository name of the extension, respectively.

2. Replace `extension_path` with the path to the directory where you want to extract the extension files.

3. Run the script regularly to check for updates and download the latest version of the extension.

## Loading the Extension into Chrome

After running the script, you'll need to load the extension into Chrome. You can do this manually by opening Chrome, navigating to `chrome://extensions`, enabling "Developer mode", clicking "Load unpacked", and selecting the directory where the extension files are located.

If you want to load the extension automatically when Chrome starts, you can modify the shortcut you use to open Chrome to include the `--load-extension` argument followed by the path to the extension directory. For example:

```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --load-extension=C:\path\to\extension
```

Please note that this will only load the extension for the current session, and it will not persist after Chrome is closed. If you completely exit Chrome or restart your computer, you'll need to open Chrome using this shortcut again to load the extension.

## Disclaimer

This script is provided as is, without warranty of any kind. Use of this script is at your own risk and responsibility.
