from VideoRepository import VideoRepository


class VideoService:
    def __init__(self):
        self.__video_repo = VideoRepository()

    def add_video(self, video):
        if self.is_valid_video(video):
            self.__video_repo.add_video(video)

    def is_valid_video(self, video):
        pass
