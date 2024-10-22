from datetime import datetime
from mongoengine import *
from profile import Profile
from Model.content import BaseContent, Platform

class BaseCollection:   
    profiles = ListField(ReferenceField(Profile))
    platform =  EnumField(Platform, required=True, error_messages={'required': 'Platform is required.'})
    duration = IntField(required=False, default=0)
    created_at = StringField(default=str(datetime.date.today()))
    completion = IntField(required=False, default=0) # se profiles.length == completion - terminou a coleta
    limit_by_profile = IntField(default=1 ,required=True, error_messages={'required': 'Limit by profile is required.'})
    contents = ListField(ReferenceField(BaseContent, required=False), default = [])
    # será usado para evitar registrar novamente conteúdo com mesmo título
    # podendo terminar coleta em todos osperfis

class InstagramDataCollection(BaseCollection):
    def __init__(self, *args, **kwargs):
        super(InstagramDataCollection, self).__init__(*args, **kwargs)
        self.platform = Platform.INSTAGRAM_POST


class YouTubeDataCollection(BaseCollection):
    def __init__(self, *args, **kwargs):
        super(InstagramDataCollection, self).__init__(*args, **kwargs)
        self.platform = Platform.YOUTUBE_VIDEO

class TikTokDataCollection(BaseCollection):
    def __init__(self, *args, **kwargs):
        super(InstagramDataCollection, self).__init__(*args, **kwargs)
        self.platform = Platform.TIKTOK
