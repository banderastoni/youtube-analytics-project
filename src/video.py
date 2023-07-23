from src.channel import Channel


class Video:
    """Класс для видео с ютуба"""

    def __init__(self, video_id):
        # билд для работы с API Youtube
        youtube = Channel.get_service()

        try:
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            self.video_id = video_id
            self.title = video_response['items'][0]['snippet']['title']
            self.url = "https://www.youtube.com/watch?v=" + video_id
            self.video_view_count = video_response['items'][0]['statistics']['viewCount']
            self.video_like_count = video_response['items'][0]['statistics']['likeCount']
        except IndexError:
            self.video_id = video_id
            self.title = None
            self.url = None
            self.video_view_count = None
            self.video_like_count = None

    def __str__(self):
        return self.title


class PLVideo(Video):
    """
    Класс плейлиста видео
    Наследник супер-класса Video
    Инициализация: "Видео ID" и "Плейлист ID"
    """

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
