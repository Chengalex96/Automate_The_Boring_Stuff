import pyautogui

# Need to select which windown is in focus

pyautogui.click(100, 100)
pyautogui.typewrite('Hello World!', interval = 0.1)

pyautogui.click(100, 100)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval = 0.1)

print(pyautogui.KEYBOARD_KEYS)

# Notes for vs code documentation
#pyautogui.press('f1')
pyautogui.hotkey('ctrl', 'o')