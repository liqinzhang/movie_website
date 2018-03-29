# -*- coding:UTF-8 -*-
#创建一个Movie对象
import webbrowser
class  Movie():
    def __init__(self,movie_title,movie_storyline,poster_image_url,trailer_youtuber_url):
        """
        :param movie_title:  电影主题
        :param movie_storyline:  电影故事描述
        :param poster_image_url: 电影url
        :param trailer_youtuber_url: 电影播放url
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_url =trailer_youtuber_url
    #打开预告片进行播放
    def show_trailer(self):
        webbrowser.open(self.trailer_url)

