
from flask import Flask
from movies_tools import *
import random
from random import sample


app = Flask(__name__)



@app.route('/')
def home():
    return '<h1>html tag: {} movies recorded.</h1>'.format(lines_count)



@app.route('/movies/ratings')
def list_movies():

    for m in movies_lst:
        m_sample = sample(movies_lst, 10)


    ret_str = ''
    for i in m_sample:
        one_mov = i
        some_movies = Movie(one_mov)
        ret_str += 'Movie: {} | IMBD Rating: {}<br>'.format(some_movies.title, some_movies.imbd)
    return ret_str






if __name__ == '__main__':
    app.run()
