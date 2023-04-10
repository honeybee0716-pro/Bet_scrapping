import time
import pyautogui
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import webbrowser
from pywinauto import Desktop, Application

# from pywinauto.application import Application
app = Application(backend = "uia").start('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
url = 'https://www.bet365.gr/#/IP/EV15550241432C1'

time.sleep(1)
pyautogui.typewrite(url, interval = 0.01)
pyautogui.press('enter')
time.sleep(7)

# webbrowser.open(url, new=2)
# win=Desktop('uia').window(title='bet365 - Online Sports Betting - Chromium')
# print('- check login button click ---------------')
# # win.print_control_identifiers()
# mouse.click(button='left', coords=(820, 119))
# # mouse.click(coords=(862, 410))
# time.sleep(2)
# username = 'qqqqq'
# password = '11111'
# pyautogui.typewrite(username, interval=0.1)
# time.sleep(0.5)
# pyautogui.press('enter')
# pyautogui.typewrite(password, interval=0.1)
# time.sleep(0.5)
# pyautogui.press('enter')
# # win.print_control_identifiers()



