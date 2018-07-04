# -*- coding: utf-8 -*-
# request for all movies
def getfilms(cur):
    cur.execute('SELECT * FROM film')
    return cur.fetchall()


# request for one movie
def getfilm(cur, id):
    cur.execute('SELECT * FROM film WHERE idFilm = ' + str(id))
    return cur.fetchone()


# request for all sessions
def getTimeFilm(cur, idFilm):
    cur.execute('SELECT * FROM session WHERE idFilm = ' + str(idFilm))
    return cur.fetchall()


# request for all seats on the session
def getPlaces(cur, id_session):
    cur.execute('SELECT * FROM place WHERE idSession = ' + str(id_session))
    return cur.fetchall()


# request for a single session
def getSession(cur, id_session):
    cur.execute('SELECT * FROM session WHERE idSession = ' + id_session)
    return cur.fetchone()


# request for change of seats in the hall
def UpdatePlace(cur, place, id_session, conn):
    cur.execute('UPDATE place SET free = 0 WHERE NumPlace = \'%s\' AND idSession = \'%s\''%(place, id_session))
    conn.commit()


# request to create a session
def createSession(cur, time, price, id_film, date, conn):
    cur.execute('INSERT INTO session (Times, Price, idFilm, Date) VALUES (\'%s\',%d,%d,\'%s\')'%(time, price, id_film, date))
    id_session = cur.lastrowid
    for j in range(50):
        cur.execute('INSERT INTO place (idSession, NumPlace) VALUES (%d,%d)'%(id_session, j + 1))
    conn.commit()


# request to edit movie data
def updateFilm(cur, film_name, film_time, id_film, conn):
    cur.execute('UPDATE film SET Duration = \'%s\' WHERE idFilm = \'%d\''%(film_time, id_film))
    cur.execute('UPDATE film SET FilmName = \'%s\' WHERE idFilm = \'%d\''%(film_name, id_film))
    conn.commit()


# request to create a movie
def createFilm(cur, film_name, film_time, age_limit, film_image, conn):
    cur.execute('INSERT INTO film (FilmName, Duration, AgeLimit, FilmImage) VALUES (\'%s\',\'%s\',\'%s\',\'%s\')'%(film_name, film_time, age_limit, film_image))
    conn.commit()

