# Webbrowser module

import webbrowser
# webbrowser.open('automatetheboringstuff.com')

import sys, pyperclip

sys.argv #['mapit.py', '870', 'Valencia']

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else: 
    address = pyperclip.paste()

# webbrowser.open('google.com/maps/place/<ADDRESS>')
webbrowser.open('www.google.com/maps/place/' + address)

# 870 valencia st copy to clipboard