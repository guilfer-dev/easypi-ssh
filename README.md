# EasyPiSSH

This app was created to easily configurate new writen Raspberry Pi SD card images.

## What it does:
 - Creates a new SSH file that enables connection via SSH on port 22.
 - Setup a wi-fi connection creating proper configuration file with SSID and Password informed by the user.

**Important:**
- The app will not validate the device or anything typed when applying the configuration
- Only works in windows machines
- Tested with Raspberry Pi OS using Windows 10 version 20H2

## How to use:
1. Install Python 3.6+ on your machine
2. Execute: `source ENV/bin/activate`
3. Execute: `pip install -r requirements.txt`
4. Execute: `python main.py`

 **Alternatively you can generate a executable file with PyInstaller (recommended)**
- After installing requirements.txt execute the command `pyinstaller --onefile  main.py`

**If you need to configure your Pi as an access point I highly recomend checking out my friend's repository** [raspap](https://github.com/davifcs/raspap)
