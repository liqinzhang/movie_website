# -*- coding:UTF-8 -*-
import media
"""导入media电影类：
主要给电影对象获取电影名称，电影故事描述、电影海报、电影播放地址
"""
import fresh_tomatoes
#创建实例
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://b-ssl.duitang.com/uploads/item/201204/30/20120430090122_kkF4x.jpeg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://img1.cache.netease.com/catchpic/E/EC/ECE77F7F43F9CA9F961E75B0B6815EE7.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")


school_of_rock = media.Movie("School of Rock","Storyline",
                             "http://img18.3lian.com/d/file/201711/07/ba146e99dfbca2f64e8c9ef6719a2f4d.png",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille","Storyline",
                          "http://img18.3lian.com/d/file/201711/07/73cd8b44628321f3cd7784260717dfad.png",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris","Storyline",
                                 "http://img18.3lian.com/d/file/201711/07/468465c3b90282e3de7d5f130740270f.jpg",
                                 "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games","Storyline",
                           "http://img18.3lian.com/d/file/201711/07/749781c2d7ab75d49fa9b165ff6ecc71.png",
                           "http://www.youtube.com/watch?v=PbA63a7H0bo")
movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]
fresh_tomatoes.open_movies_page(movies)
