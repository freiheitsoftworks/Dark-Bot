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
        
    def get_profile_page_info():
        bot.locateCenterOnScreen # usar pyautogui para clickar baseado nas imagens salvas em static assets
        bot.click(x=1920, y=1080) # posiciona o cursor no centro da tela
        time.sleep(1)
        bot.scroll(-500) # rola para baixo 500 pixels
        time.sleep(1)
        bot.scroll(-500) # rola para baixo mais 500 pixels
        # deve clickar no mais
        # deve clickar colocar mouse no centro da pagina
        # rolar container até o final
        # depois segurar esquerdo até o final do container e soltar
        # copiar informaçoes e usar para criar novo profile (no serviço de criar profile)
