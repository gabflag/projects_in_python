import webbrowser
import pyautogui 
import time


url = 'https://pt.englishcentral.com/lessons'

webbrowser.open(url)

time.sleep(10)
pyautogui.doubleClick(681, 304)
time.sleep(15)

pyautogui.click(670, 593)
time.sleep(2)

pyautogui.click(644, 206)
#finished
