from .youtube import YoutubeProfile as ytp
from models.profile import Profile

class CreateProfile():
    def execute(url):   
        ytp.open_brave_browser()
        ytp.open_channel(url)
        profileInfo = ytp.get_profile_page_info()
        # falta buscar no banco por perfil com mesmo nome, plataforma ou url igual
        # para impedir que haja duplicação
        profile = Profile(url = profileInfo.url)

        return profile