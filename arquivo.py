import pyautogui
from time import sleep
import webbrowser
import os

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chrome_path).open("https://web.whatsapp.com/")
sleep(5)

pyautogui.click(384,108)
