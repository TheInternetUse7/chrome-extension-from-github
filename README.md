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

3. Run the script regularly to check for updates and download the latest version of the extension. You can automate this process using a task scheduler or cron job, or you can manually run the script whenever you want to check for updates.

# Loading the Extension into Chrome

After the script has downloaded and extracted the extension, you’ll need to manually load the extension into Chrome. Here’s how:

1. Open Chrome and navigate to `chrome://extensions`.

2. Enable “Developer mode”.

3. Click “Load unpacked” and select the directory where the extension files were extracted by the script.

Chrome should now load the extension, and it will continue to do so every time it starts up, as long as the location of the extension files remains the same. This means that whenever the script downloads a new version of the extension, Chrome will automatically load the updated version the next time it starts.

## Disclaimer

This script is provided as is, without warranty of any kind. Use of this script is at your own risk and responsibility.
