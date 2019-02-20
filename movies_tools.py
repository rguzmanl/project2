#-*- coding: utf-8 -*-
import csv
import random
from random import sample




movies_lst = []
with open('movies_clean.csv', 'r', encoding='utf8') as fpython:
    movie_lines = csv.reader(fpython, delimiter=',')
    header = next(movie_lines, None)

    lines_count = 0
    for l in movie_lines:
        movies_lst.append(l)
        lines_count += 1
    # print(lines_count)




class Movie:

    def __init__(self, a_movie):
        self.title = a_movie[0]
        self.director = a_movie[12]
        self.release = a_movie[5]
        self.imbd = a_movie[-2]


    def __str__ (self):
        return 'MOVIE: {}, DIRECTOR: {}, REALAESE: {}, IMBD RATING: {}'.format(self.title, self.director, self.release, self.imbd)




print('\n  *** Instance was created in the source code of the Class Movie *** \n')

print ("\n***** TESTS *****\n")

####### The code below creates one instance of class Movie

# random_mov = random.choice(movies_lst)
# print(random_mov)
# print(Movie(random_mov))
# print(type(Movie(random_mov)))

####### This is an attempt to create 10 random instances of the class Movie

# short_lst = []
# for m in movies_lst:
#     m_sample = sample(movies_lst, 10)
#     # print(m_sample)
# for i in m_sample:
#     #print(i)
#     one_mov = i
#     #print(one_mov)
#     #print(Movie(one_mov))
#     some_movies = Movie(one_mov)
#     print(type(some_movies))
#     #print(some_movies)
#     #short_lst.append(Movie(one_mov))








#
