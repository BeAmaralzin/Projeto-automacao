import pyautogui
from time import sleep
import webbrowser
import time

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chrome_path).open("https://web.whatsapp.com/")
sleep(8)

imagem = r'C:\Users\bamar\Downloads\imagemwpp.jpg'

def aguardar_imagem(caminho_imagem, timeout=30):
    """Aguarda uma imagem aparecer na tela com timeout."""
    inicio = time.time()
    while True:
        localizacao = pyautogui.locateOnScreen(caminho_imagem, confidence=0.8)
        
        if localizacao:
            print(f"Imagem encontrada! O WhatsApp carregou.")
            return localizacao
        if time.time() - inicio > timeout:
            print("Tempo esgotado: O WhatsApp não carregou a tempo.")
            return None
            
        sleep(1) 

localizacao = aguardar_imagem(imagem)
if localizacao:
    pyautogui.click(localizacao)
else:
    print("Erro ao carregar.")

