from datetime import datetime
from mongoengine import *

class Profile:
    name = StringField(required=False, error_messages={'required': 'Name is required.'})
    niche = StringField(required=False, error_messages={'required': 'Niche is required.'})
    sub_niche = StringField(required=False, error_messages={'required': 'Sub niche is required.'})
    contents_per_day = FloatField(default=0,required=False)
    contents_per_week = FloatField(default=0,required=False)
    contents_per_month = FloatField(default=0,required=False)
    total_contents = IntField(default=0,required=False)
    comments_average = FloatField(default=0,required=False)
    similar_channels = ListField(ReferenceField('Profile'), required=False,default = [])
    synchronized_channels = ListField(ReferenceField('Profile'), required=False,default = [])
    last_content_date = StringField(required=False,default=datetime.now())
    last_content = ReferenceField("Content",required=False,default=None)
    main_language = StringField(required=False,default="pt-BR")
    url = StringField(required=True, error_messages={'required': 'Url is required.'})
    subscribes = IntField(default=0,required=False)
    views = IntField(default=0,required=False)
    n_contents = IntField(default=0,required=False)
    start_date = StringField(required=False,default=datetime.now())
    platform =  EnumField("Platform", required=True, error_messages={'required': 'Platform is required.'})
