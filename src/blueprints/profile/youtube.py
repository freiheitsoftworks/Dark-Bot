# script de automação de coleta de dados de 1 perfil de youtube
# documentação pyautogui: https://pyautogui.readthedocs.io/
# import cv2
# import selenium
import time
import pyautogui as bot

class YoutubeProfile:
    def open_brave_browser():
        bot.press('win') # abri o command
        time.sleep(0.5)
        bot.write(["b","r","a","v","e"], interval=0.1) # digita braver no explorer de pastas
        time.sleep(0.5)
        bot.press('enter') # abre braver
        time.sleep(2)
        with bot.hold('ctrl'):
            bot.press(['t']) # abre nova guia selecionando barra de busca
        time.sleep(0.5)
    
    def open_channel(url):
        writable_url = list(url) # se torna um array de caracteres
        bot.write(writable_url) # digita  url
        time.sleep(0.5)
        bot.press(['enter']) # busca com enter


