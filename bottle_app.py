import sqlite3
import assets_route
from bottle import route, run, debug, template, request, static_file, error, get, default_app

horder = '/home/jmao/horder/'
@route('/')
def load():
    return static_file('index.html', root=horder)

################################################################################
@route('/login')
def login():
    return template(horder + 'views/login.tpl')

################################################################################

@route('/signup')
def signup():
    return template(horder + '/views/signup.tpl')


################################################################################

@route('/dashboard')
def dashboard():
    return template(horder + 'views/dashboard.tpl')


################################################################################


@error(403)
def mistake(code):
    return 'The parameter you passed has the wrong format!'


debug(True)
application = default_app()
#run(reloader=True)

