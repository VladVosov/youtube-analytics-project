import json
import os
import apiclient
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')
    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.id = self.channel["items"][0]["id"] #id канала
        self.title = self.channel["items"][0]["snippet"]["title"] #название канала
        self.description = self.channel["items"][0]["snippet"]["description"] #описание канала
        self.url = self.channel["items"][0]["snippet"]["thumbnails"]["default"]["url"] #ссылка на канал
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"] #количество подписчиков
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"] #количество видео
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"] #общее количество просмотров

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_info = json.dumps(self.channel, indent=2, ensure_ascii=False)
        print(channel_info)

    def to_json(self, file):
        to_json = {"id": self.id, "title": self.title, "description": self.description, "url": self.url,
                   "subscriber_count": self.subscriber_count, "video_count": self.video_count,
                   "view_count": self.view_count}
        with open('moscowpython.json', 'w') as file:
            file.write(json.dumps(to_json))


    @classmethod
    def get_service(cls):
        return apiclient

moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
print(moscowpython.channel)
print(Channel.get_service())

