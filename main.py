import win32api

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\\\000')[:-1]

print('Drive available:')

for i, val in enumerate(drives):
    print(f'{i} - {val}')


def evaluate_input():
    try:
        location = int(input('Please, select the drive your SD card\n'))
        if location >= len(drives):
            print('invalid drive selected')
            evaluate_input()
        else:
            print(f'Writing on {drives[location]}')

            print('Creating SSH file')
            ssh = open(f"{drives[location]}\\ssh", "w")
            ssh.close()
            print('** SSH file created or overwritten if already exists **\n')

            ccode = input('Please enter your country code.\n').upper()
            ssid = input('Please enter the SSID of your network connection\n')
            password = input('Please enter the PASSWORD of your network connection\n')
            print('\nCreating wpa_supplicant.conf file')

            wapconf = open(f"{drives[location]}\\wpa_supplicant.conf", "wb")
            wapconf.write(
                'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n'
                'update_config=1\n'
                f'country={ccode}\n'
                'network={\n'
                f' ssid="{ssid}"\n'
                f' psk="{password}"\n'
                '}'.encode(encoding="utf-8", errors="strict"))
            wapconf.close()
            print(
                '** wpa_supplicant.conf file created overwritten if already exists**\n'
                '\n'
                'Your Raspberry Pi is ready to connect to your network with SSH enabled\n'
                '                  \n'
                '**Remember**\n'
                'Default User: pi\n'
                'Default Password: raspberry')

    except ValueError:
        print('Invalid Input')
        evaluate_input()


evaluate_input()
input('\nPress any key to close... ')
