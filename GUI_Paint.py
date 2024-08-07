import pyautogui

# Click F5 with VS code as the focus

pyautogui.click()

distance  = 500

while distance >0:

    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration= 0.5)
    distance = distance - 25

    print(0, distance)
    pyautogui.dragRel(0, distance,duration= 0.5)
    distance = distance - 25
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration= 0.5)
    distance = distance - 25
    print(0, -distance)
    pyautogui.dragRel(0,  -distance, duration= 0.5)
    distance = distance - 25

    # If mouse at top left, will raise exception error - failsafe