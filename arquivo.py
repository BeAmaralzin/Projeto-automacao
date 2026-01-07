import pyautogui
from time import sleep

def abrir_navegador():
    # Abre o navegador (exemplo com Google Chrome)
    pyautogui.press('win')
    sleep(1)
    pyautogui.write('chrome')
    sleep(1)
    pyautogui.press('enter')
    sleep(3)  # Espera o navegador abrir
