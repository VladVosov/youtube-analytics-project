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
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.id = self.channel["items"][0]["id"]  # id канала
        self.title = self.channel["items"][0]["snippet"]["title"]  # название канала
        self.description = self.channel["items"][0]["snippet"]["description"]  # описание канала
        self.url = self.channel["items"][0]["snippet"]["thumbnails"]["default"]["url"]  # ссылка на канал
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"]  # количество подписчиков
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]  # количество видео
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]  # общее количество просмотров

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

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

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, value):
        self.__channel_id = value

    @classmethod
    def get_service(cls):
        return apiclient
