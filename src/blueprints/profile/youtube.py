import time
import pyautogui
import pyperclip

from utils.date import yt_date_to_datetime

class YoutubeProfile:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()  # Obtém a resolução da tela
        self.center_x = self.screen_width / 2
        self.center_y = self.screen_height / 2

    def open_brave_browser():
        pyautogui.press('win') # abri o command
        time.sleep(0.5)
        pyautogui.write(["b","r","a","v","e"], interval=0.1) # digita braver no explorer de pastas
        time.sleep(0.5)
        pyautogui.press('enter') # abre braver
        time.sleep(2)
        with pyautogui.hold('ctrl'):
            pyautogui.press(['t']) # abre nova guia selecionando barra de busca
        time.sleep(0.5)
    
    def open_channel(url):
        writable_url = list(url) # se torna um array de caracteres
        pyautogui.write(writable_url) # digita  url
        time.sleep(0.5)
        pyautogui.press(['enter']) # busca com enter
    
        
    def get_profile_page_info(self):
        see_more_location = pyautogui.locateCenterOnScreen('assets/youtube/see_more_youtube_profile.png')
        if see_more_location is None:
            print("See more location not found.")
            return None
        pyautogui.click(see_more_location) # clickou em ""...mais/...more" # apenas para portugues PT BR
        time.sleep(1.5)
        pyautogui.moveTo(self.center_x, self.center_y)
        pyautogui.scroll(-1000) # rolou até o final do container
        time.sleep(0.2)
        
        subscribes_location = pyautogui.locateCenterOnScreen('assets/youtube/subscribes.png')
        videos_location = pyautogui.locateCenterOnScreen('assets/youtube/videos.png')
        views_location = pyautogui.locateCenterOnScreen('assets/youtube/views.png')
        channel_start_date_location = pyautogui.locateCenterOnScreen('assets/youtube/channel_start_date.png')
        if subscribes_location is None or videos_location is None or views_location is None or channel_start_date_location is None:
            if subscribes_location is None:
                print("Subscribes location not found.")
            if videos_location is None:
                print("Videos location not found.")
            if views_location is None:
                print("Views location not found.")
            if channel_start_date_location is None:
                print("Channel start date location not found.")
            return None

        ############### PEGANDO SUBSCRIBES #################
        pyautogui.move(subscribes_location.x + 100,subscribes_location.y)
        pyautogui.press("left", presses=3, interval=0.1)
        with pyautogui.hold('ctrl'):
            pyautogui.press('c')        
        divided_content = pyperclip.paste().split(" ")
        p1 = float(divided_content[0].replace(",","").replace(".","")) # apenas para portugues PT BR
        p2 =  1000000 if divided_content[1] == "mi" else 1000 if divided_content[1] == "mil" else 1 # apenas para portugues PT BR
        subscribes_data = p1 * p2
        print("subscribes_data:",subscribes_data)

        ############### PEGANDO Nº DE VIDEOS #################
        pyautogui.move(videos_location.x + 100, videos_location.y)
        pyautogui.press("left", presses=3, interval=0.1)
        with pyautogui.hold('ctrl'):
            pyautogui.press('c')        
        divided_content = pyperclip.paste().split(" ")
        p1 = float(divided_content[0].replace(".",""))
        videos_data = p1
        print("videos_data:",videos_data)
        
        ############### PEGANDO Nº DE VIEWS #################
        pyautogui.move(views_location.x + 100, views_location.y)
        pyautogui.press("left", presses=3, interval=0.1)
        with pyautogui.hold('ctrl'):
            pyautogui.press('c')        
        divided_content = pyperclip.paste().split(" ")
        p1 = float(divided_content[0].replace(".",""))
        views_data = p1
        print("views_data:",views_data)

        ############### PEGANDO DATA DE INÍCIO DO CANAL #################
        pyautogui.move(channel_start_date_location.x + 100, channel_start_date_location.y)
        pyautogui.press("left", presses=3, interval=0.1)
        with pyautogui.hold('ctrl'):
            pyautogui.press('c')        
        divided_content = pyperclip.paste().split(" ")
        date_array = divided_content[2:6] # subarray com a data
        date_string = " ".join(date_array) # string com a data
        start_date = yt_date_to_datetime(date_string)
        print("start_date:",start_date)
        return {
            'subscribes': subscribes_data,
            'videos': videos_data,
            'views': views_data,
            'start_date': start_date
        }