#!/usr/bin/env python3

"""
Author: @synfinner (gtfkd.com)
Shout out to @josh_penny and @TLP_R3D for discovering panels and their subsequent work.
Description: This script attempts to download all files from a Bandit Stealer panel.
"""
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# Replace 'http://localhost:8080' with the appropriate IP and port. SSL warnings are disabled.
base_url = 'http://localhost:8080'

# Fetch the builds data
response = requests.get(f'{base_url}/builds', verify=False)
data = response.json()
for i in data:
    file_name = i['name']
    file_url = f'{base_url}/builds/download?fileName={file_name}'
    response = requests.post(file_url, verify=False)
    if response.status_code == 200:
        binData = response.content
        with open(file_name, 'wb') as f:
            f.write(binData)
            print(f'Successfully downloaded: {file_name}')
    elif response.status_code == 405:
        try:
            file_url = f'{base_url}/downloads?fileName={file_name}'
            response = requests.get(file_url, verify=False)
            if response.status_code == 200:
                binData = response.content
                with open(file_name, 'wb') as f:
                    f.write(binData)
                    print(f'Successfully downloaded: {file_name}')
        except:
            print(f'Failed to download: {file_name}')