# -*- coding: utf-8 -*-
# we connect libraries
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import ctypes, module

# connect to flask
app = Flask(__name__)

# connect to the database
mysql = MySQL()
mysql.__init__(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'SergeyElmanov'
app.config['MYSQL_DATABASE_DB'] = 'cinema'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8'
conn = mysql.connect()
cur = conn.cursor()


# create URL (routes)
@app.route('/')
# function tied to the route
# Homepage
def hellouser():
    # Simple static page rendering
    return render_template('hellouser.html')


@app.route('/sell')
# page of film selection
def sell():
    # query the database
    film = module.getfilms(cur)
    return render_template('sell.html', film=film)


@app.route('/FilmTime')
# movie date selection page
def FilmTime():
    # retrieving data from a page
    idFilm = request.args.get('film')
    # if there is no such movie, we'll send it to the error page
    if idFilm == None: return render_template('404.html')
    session = module.getTimeFilm(cur, idFilm)
    film = module.getfilm(cur, idFilm)
    # if the movie does not exist in the database, then the error page
    if film == None: return render_template('404.html')
    # if the movie is 18+, then for testing
    if film[3] == '18+': return render_template('ageLimit.html', film=film)
    return render_template('FilmTime.html', session=session, film=film)


@app.route('/Film18Time')
# page for selecting the date of the film, if the film is 18+
def Film18Time():
    idFilm = request.args.get('film')
    # if there is no such movie, we'll send it to the error page
    if idFilm == None: return render_template('404.html')
    session = module.getTimeFilm(cur, idFilm)
    film = module.getfilm(cur, idFilm)
    # if the movie does not exist in the database, then the error page
    if film == None: return render_template('404.html')
    return render_template('FilmTime.html', session=session, film=film)


@app.route('/places')
# site selection page
def places():
    id_session = request.args.get('id_session')
    # if there is no such session, we'll send it to the error page
    if id_session == None: return render_template('404.html')
    session = module.getSession(cur, id_session)
    # if the session does not exist in the database, then the error page
    if session == None: return render_template('404.html')
    film = module.getfilm(cur, session[3])
    # place request
    places = module.getPlaces(cur, session[0])
    return render_template('places.html', session=session, film=film, place=places)


@app.route('/buy', methods=['GET', 'POST'])
# purchase function
def buy():
    id_session = request.args.get('id_session')
    places = list(map(int, request.args.get('places').split(',')))
    for i in range(len(places)):
        place = places[i]
        # change in the database of places
        module.UpdatePlace(cur, place, id_session, conn)
    return 'ok'


# running flask
if __name__ == '__main__':
    app.run()
