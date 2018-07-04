# -*- coding: utf-8 -*-
# we connect libraries
from cinema import cur, conn
import module
import sys

if __name__ == '__main__':
    # if there are more than two arguments, then exit
    if len(sys.argv) < 2:
        sys.exit()
    # if the argument is such, then create a session
    if sys.argv[1] == 'session:create':
        time = input('Time: ')
        price = int(input('Price: '))
        id_film = int(input('idFilm: '))
        date = input('Date: ')
        module.createSession(cur, time, price, id_film, date, conn)
    # if the argument is this, then change the movie
    if sys.argv[1] == 'film:update':
        film_name = input('FilmName = ')
        film_time = input('Duration = ')
        id_film = int(input('idFilm = '))
        module.updateFilm(cur, film_name, film_time, id_film, conn)
    # if the argument is this, then create a movie
    if sys.argv[1] == 'create:film':
        film_name = input('FilmName = ')
        film_time = input('Duration = ')
        age_limit = input('AgeLimit = ')
        film_image = input('FilmImage(../static/image/*.jpg(png ...)) = ')
        module.createFilm(cur, film_name, film_time, age_limit, film_image, conn)
    # if there are no arguments, output an error
    else:
        print('Command error')
