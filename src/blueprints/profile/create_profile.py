from utils.enums import Platform
from utils.response import Response
from .youtube import YoutubeProfile as ytp
from mongoengine import *
from models.profile import Profile

class CreateProfile():
    def execute(url, platform): 
        try:
            if(platform == Platform.YOUTUBE_VIDEO):
                existing_profile = Profile.objects(url=url).first()
                if existing_profile:
                    return f"O canal já está registrado"


                ytp.open_brave_browser()
                ytp.open_channel(url)
                profileInfo = ytp.get_profile_page_info()

                profile = Profile(
                    url=url,
                    subscribes=profileInfo['subscribes'],
                    n_contents=profileInfo['videos'],
                    views=profileInfo['views'],
                    start_date=profileInfo['start_date'],
                    platform=platform,
                )
                profile.save()
                return Response.right(message=f"Perfil criado com sucesso: {profile.url}")
            else:
                return Response.left( message= f"Plataforma {platform.value} não suportada", status=400)
        except Exception as error:
            return Response.left( message=f"Erro ao processar dados: {error}", status= 500)
