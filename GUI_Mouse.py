# Graphical User Interface (GUI) Automation

# X/Y coordinates, with the top left being 0, 0

import pyautogui
print(pyautogui.size()) #1920, 1080

width, height = pyautogui.size()

# It starts from 0 so the bottomright corner is 1919, 1079

print(pyautogui.position())

# Absolute positon
pyautogui.moveTo(10,10, duration = 1.5) # gradually move with duration

# relative position
pyautogui.moveRel(500, 50, duration = 2)

pyautogui.moveRel(-200, -50, duration = 2)

# Ctrl F5 to run

print(pyautogui.position()) # 310, 10

pyautogui.click(310, 10) # dont need arguments for click

# pyautogui.doubleClick(310, 10)

# In terminal: 
pyautogui.displayMousePosition()