import pyautogui

print(pyautogui.screenshot())

pyautogui.screenshot('screenshot_Example.png') # saves the screenshot

print(pyautogui.locateOnScreen('Calc7key.png')) # With calculator

# Returns location of the 7 key: width, ehight of screen, width of shape, height of shape

print(pyautogui.locateCenterOnScreen('Calc7key.png')) # With calculator

# Has to be pixel perfect match to locate, also computationally expensive

pyautogui.moveTo(1568, 596, duration = 1.5)

pyautogui.click()

# If it can't find anything, will return nothing