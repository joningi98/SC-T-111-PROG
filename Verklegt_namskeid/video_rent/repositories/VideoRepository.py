from Video import Video


class VideoRepository:

    def __init__(self):
        self.__videos = []

    def add_video(self, video):
        with open("./data/videos.txt", "a+") as videos_file:
            title = video.get_title()
            genre = video.get_genre()
            length = video.get_length()
            videos_file.write("{},{},{}\n".format(title, genre, length))