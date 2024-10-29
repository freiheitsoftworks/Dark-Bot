# script de automação de coleta de dados de 1 perfil de youtube
# documentação pyautogui: https://pyautogui.readthedocs.io/
# import cv2
# import selenium
import time
import pyautogui as bot

class YoutubeDataCollection:
    def openBraveBrowser():
        bot.press(['home'])
        time.sleep(0.22)
        bot.write('brave')
        time.sleep(0.22)
        bot.press('enter')
        time.sleep(0.22)
        print("abriu brave?")