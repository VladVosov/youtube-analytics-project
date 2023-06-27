import os
from googleapiclient.discovery import build


class Video:
    """Класс для ютуб-видео"""
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')
    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_video):
        self.id_video = id_video
        self.video = self.youtube.videos().list(id=self.id_video, part='snippet,statistics').execute()
        self.id = self.video['items'][0]['id']
        self.name = self.video['items'][0]['snippet']['title']
        self.url = self.video['items'][0]['snippet']['thumbnails']['standard']['url']
        self.view_count = self.video['items'][0]['statistics']['viewCount']
        self.like_count = self.video['items'][0]['statistics']['likeCount']


class PLVideo(Video):
    def __init__(self, id_video, id_PL):
        super().__init__(id_video)
        self.id_PL = id_PL
        self.playlist_response = self.youtube.playlists().list(id=id_PL, part='snippet, contentDetails').execute()
        self.playlist_items = self.youtube.playlistItems().list(playlistId=id_PL,
                                                                part='snippet, contentDetails').execute()
        self.id = self.playlist_items['items'][0]['id']
        self.title = self.playlist_items['items'][0]['snippet']['title']
        self.url = f"https://youtu.be/{id_video}"
        self.view_count = self.video["items"][0]["statistics"]["viewCount"]
        self.like_count = self.video["items"][0]["statistics"]["likeCount"]
        self.id_PL = self.playlist_response['items'][0]['id']
