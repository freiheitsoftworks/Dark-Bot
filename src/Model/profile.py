# models/profile.py

from datetime import datetime


class Profile:
    def __init__(self, id, name, main_language, subscribers, niche, subniche):
        self.id = id
        self.name = name
        self.main_language = main_language
        self.subscribers = subscribers
        self.niche = niche
        self.subniche = subniche
        self.videos_per_day = 0
        self.videos_per_week = 0
        self.videos_per_month = 0
        self.total_videos = 0
        self.comments_average = 0
        self.similar_channels = []
        self.synchronized_channels = []
        self.last_update = None
        self.last_video = None

    def update_video(self, video_id):
        self.last_video = video_id
        self.last_update = datetime.now()
        self.total_videos += 1  # Update as needed
