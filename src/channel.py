import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')

    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel_id = channel_id
        self.title = channel['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/channel/' + channel_id
        self.description = channel['items'][0]['snippet']['description']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        """Геттер channel_id"""
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращающий объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, file):
        """Метод, сохраняющий в файл значения атрибутов экземпляра класса"""
        with open(file, 'w') as fp:
            json.dump(self.__dict__, fp, indent=2, ensure_ascii=False)
