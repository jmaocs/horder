import sqlite3
import assets_route
from bottle import route, run, debug, template, request, static_file, error, get, default_app

horder = '/home/Abdulmalek/mysite/horder/'
@route('/')
def load():
    return static_file('index.html', root=horder)

################################################################################
@route('/login', method='GET')
def login():
    return template(horder + 'views/login.tpl')

################################################################################

@route('/signup', method='GET')
def signup():

    if request.GET.get('signup','').strip():

        new = request.GET.get('fname', '').strip()
        new2 = request.GET.get('lname', '').strip()
        new3 = request.GET.get('email', '').strip()

        conn = sqlite3.connect('/home/Abdulmalek/mysite/horder/db/user.db')
        c = conn.cursor()
        c.execute("INSERT INTO user (first_name,last_name, email) VALUES (?,?,?)", (new,new2,new3))

        conn.commit()
        c.close()

        return 'Your registration is completed %s' % new
        
    else:
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
