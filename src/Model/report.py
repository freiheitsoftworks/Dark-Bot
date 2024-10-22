# models/report.py

class Report:
    def __init__(self, report_type, data):
        self.report_type = report_type
        self.data = data

class InstagramReport(Report):
    def __init__(self, data):
        super().__init__("Instagram Report", data)

class YouTubeReport(Report):
    def __init__(self, data):
        super().__init__("YouTube Report", data)
