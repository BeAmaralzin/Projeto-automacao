import pyautogui
from time import sleep

pyautogui.FAILSAFE = True

def abrir_navegador():
    pyautogui.press('win')
    sleep(0.5)
    pyautogui.write('chrome')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.write('https://web.whatsapp.com/')
    pyautogui.press('enter')

abrir_navegador()

