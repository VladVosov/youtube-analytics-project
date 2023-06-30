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
        video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',id=id_video).execute()
        self.title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = video_response['items'][0]['statistics']['commentCount']

    def __str__(self):
        return self.title

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))

    @staticmethod
    def __printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""

        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))



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
        self.id_PL = self.playlist_response['items'][0]['id']