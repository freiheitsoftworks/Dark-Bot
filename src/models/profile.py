from datetime import datetime
from mongoengine import *
from Model.content import BaseContent

class Profile:
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