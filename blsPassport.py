import webbrowser
import pyautogui
import time
import requests

webbrowser.register(
    "chrome",
    None,
    webbrowser.BackgroundBrowser(
        "C://Program Files//Google//Chrome//Application//chrome.exe"
    ),
)
webbrowser.get("chrome").open(
    "https://www.blsindia-canada.com/appointmentbls/appointment.php"
)
# wait to load the page
time.sleep(3)

# click first drop down
pyautogui.click(977, 374)
# click Toronto
# pyautogui.click(935, 512, duration = 0.5)
# click Surry to just check open slots
pyautogui.click(935, 490, duration=0.5)
# click second drop down
pyautogui.click(938, 408, duration=0.5)
# click Passport
pyautogui.click(933, 448, duration=0.5)

# wait for white overlay
time.sleep(2)
# click Calendar
pyautogui.click(918, 444, duration=0.5)
time.sleep(3)

found_flag = False
arrow_flag = False

for k in range(0, 12):
    x = 897
    y = 519
    if arrow_flag:
        break
    try:
        for j in range(0, 6):
            if found_flag:
                break
            for i in range(0, 7):
                pyautogui.moveTo(x, y)
                x, y = pyautogui.position()
                r, g, b = pyautogui.pixel(x, y)
                # if (r == 247 and g == 247 and b == 247):
                #     print("grey")
                # elif (r == 255 and g == 128 and b == 0):
                #     print("orange")
                # elif (r == 252 and g == 197 and b == 198):
                #     print("red")
                # elif (r == 66 and g == 139 and b == 202):
                if r == 66 and g == 139 and b == 202:
                    print("Slot found!")
                    r = requests.get(
                        "https://trigger.macrodroid.com/{MacroDroid-device-id-goes-here}/slotopen"
                    )
                    found_flag = True
                    arrow_flag = True
                    break
                x = x + 44
            x = 897
            y = y + 25
        # detect next arrow to open next month calendar
        start = pyautogui.locateCenterOnScreen("next_arrow.png")
        pyautogui.click(start)
    except:
        print("No dates available on next month. Exiting.")
        pyautogui.hotkey("ctrl", "w")
        arrow_flag = True


