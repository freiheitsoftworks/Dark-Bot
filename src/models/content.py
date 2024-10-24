from datetime import datetime
from enum import Enum
from mongoengine import *
from profile import Profile
from data_collection import BaseCollection

class Platform(Enum):
    YOUTUBE_VIDEO = "YouTube Video"
    TIKTOK = "TikTok"
    INSTAGRAM_POST = "Instagram Post"


class Comment(Document):
    text = StringField(required=True, error_messages={'required': 'Author is required.'})
    likes = IntField(required=True, default=0, error_messages={'required': 'Invalid Likes.'})
    created_at = StringField(default=str(datetime.date.today()))
    baseContent = ReferenceField("BaseContent", reverse_delete_rule=CASCADE, required=True)
    content_url= StringField(required=True, error_messages={'required': 'Content URL is required.'})
    language = StringField(required=False,default="pt-BR")

class BaseContent(Document):
    title = StringField(required=True, error_messages={'required': 'Title is required.'})
    created_at = StringField(default=str(datetime.date.today()))
    url = URLField(required=True, error_messages={'required': 'Invalid URL.'})
    profile = ReferenceField(Profile, reverse_delete_rule=CASCADE, required=True)
    likes = IntField(required=True, default=0, error_messages={'required': 'Invalid Likes.'})
    comments = ListField(ReferenceField("Comment"))
    collection = ReferenceField(BaseCollection, reverse_delete_rule=CASCADE, required=True)
    language = StringField(required=False,default="pt-BR")


class YoutubeVideo(BaseContent):
    description = StringField(required=True, error_messages={'required': 'Description is required.'})
    duration = IntField(required=False, default=0)
    caption = StringField(required=False)
    def __init__(self, *args, **kwargs):
        super(YoutubeVideo, self).__init__(*args, **kwargs)
        self.platform = Platform.YOUTUBE_VIDEO  # Define a plataforma como YouTube

class TikTokVideo(BaseContent):
    duration = IntField(required=False, default=0)
    description = StringField(required=True, error_messages={'required': 'Description is required.'})
    caption = StringField(required=False)
    def __init__(self, *args, **kwargs):
        super(TikTokVideo, self).__init__(*args, **kwargs)
        self.platform = Platform.TIKTOK

class InstagramPost(BaseContent):
    text = StringField(required=False)
    def __init__(self, *args, **kwargs):
        super(InstagramPost, self).__init__(*args, **kwargs)
        self.platform = Platform.INSTAGRAM_POST