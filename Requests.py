# Requests Module

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(res.status_code) # 200 means downloaded ok

print(len(res.text))

print(res.text[:500])

print(res.raise_for_status()) # will return 404 error if the link doesn't exist

# Must use write-binary code
playFile = open('RomeoandJuliet.txt', 'wb')

# Passing on 100,000 bytes
for chunk in res.iter_content(100000): # Save file using iter_content

    playFile.write(chunk)
