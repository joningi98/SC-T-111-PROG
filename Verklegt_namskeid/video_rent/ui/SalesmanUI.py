from services.VideoService import VideoService
from models.Video import Video


class salesmanUI:
    def __init__(self):
        self.__video_service = VideoService()

    def main_menu(self):

        action = ""
        while action != "q":
            print("You can do the following: ")
            print("2. Add a video")
            print("Press q to quit")

            action = input("Choose an option: ").lower()

            if action == "1":
                title = input("Movie title: ")
                genre = input("Genre: ")
                length = input("Length in minutes: ")
                new_video = Video(title, genre, length)
                self.__video_service.add_video(new_video)
