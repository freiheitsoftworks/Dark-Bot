    name = StringField(required=True, error_messages={'required': 'Name is required.'})
    niche = StringField(required=True, error_messages={'required': 'Niche is required.'})
    sub_niche = StringField(required=True, error_messages={'required': 'Sub niche is required.'})
    contents_per_day = FloatField(default=0,required=False)
    contents_per_week = FloatField(default=0,required=False)
    contents_per_month = FloatField(default=0,required=False)
    total_contents = IntField(default=0)
    comments_average = FloatField(default=0)
    similar_channels = ListField(ReferenceField('Profile'), required=True,default = [])
    synchronized_channels = ListField(ReferenceField('Profile'), required=True,default = [])
    last_content_date = StringField(required=False,default=datetime.datetime.now())
    last_content = ReferenceField(BaseContent,required=False,default=None)
    main_language = StringField(required=False,default="pt-BR")

from datetime import datetime
from enum import Enum
from mongoengine import *
from profile import Profile
from Model.content import Platform
from data_collection import BaseCollection

class Report:
    def __init__(self, report_type, data):
        self.data = data

class InstagramPostReport(Report):
    most_used_coments = StringField()
    def __init__(self, *args, **kwargs):
        super(InstagramPostReport, self).__init__(*args, **kwargs)
        self.platform = Platform.INSTAGRAM_POST  # Define a plataforma como YouTube

class TikTokReport(Report):
    def __init__(self, *args, **kwargs):
        super(InstagramPostReport, self).__init__(*args, **kwargs)
        self.platform = Platform.TIKTOK  # Define a plataforma como YouTube

class YouTubeVideoReport(Report):
    def __init__(self, *args, **kwargs):
        super(YouTubeVideoReport, self).__init__(*args, **kwargs)
        self.platform = Platform.YOUTUBE_VIDEO  # Define a plataforma como YouTube