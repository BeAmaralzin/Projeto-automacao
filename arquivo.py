import pyautogui
from time import sleep
import webbrowser
import time
import pandas as pd

pyautogui.FAILSAFE = True

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chrome_path).open("https://web.whatsapp.com/")

print("Aguardando WhatsApp Web carregar...")
sleep(8)  

planilha = pd.read_excel(r'C:\Users\bamar\Downloads\planilha 2.xlsx',sheet_name='Planilha2')

for linha in planilha.index:    
        numero = planilha.loc[linha, 'TELEFONE']
        sleep(0.3)
        candidato = planilha.loc[linha, 'CANDIDATO']
        sleep(0.3)
        prazo_final = planilha.loc[linha, 'PRAZO FINAL']
        sleep(0.3)
        email = planilha.loc[linha, 'EMAIL']
        sleep(0.3)

        pyautogui.click(x=382, y=109)  

        sleep(2)
        pyautogui.write(numero)
        sleep(2)
        pyautogui.press('enter')
        sleep(2) 
        
        mensagem = f"Olá {candidato}, tudo bem? Gostaria de informar que o prazo final para envio dos documentos é {prazo_final}. Por favor, envie os documentos para o email {email}. Obrigado!"    
        sleep(2)
        pyautogui.write(mensagem)
        sleep(2)
        pyautogui.press('enter')
        sleep(2)  
        
        print(f"Mensagem enviada para {numero}\n")

