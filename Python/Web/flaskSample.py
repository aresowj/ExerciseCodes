#coding = utf-8
__author__ = 'aresowj'

'''
A very simple sample of web app using flask.
'''

from flask import Flask
from flask import request

#Initiate app instance.
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return '<H1>Homepage</H1>'
	
@app.route('/signin', methods=['GET'])
def signin_form():
	return '''<form action="/signin" method="post">
			<p>Username: <input name="username"></p>
			<p>Password: <input name="password" type="password"></p>
			<p><button type="submit">Sign in</button></p>
			</form>'''
			
@app.route('/signin', methods=['POST'])
def sigin():
	#Compare the input directly.
	if request.form['username']=='kagami' and request.form['password']=='123':
		return '<h3>Login succeed.'
	else:
		return '<h3>Bad username or password.</h3>'

if __name__ == '__main__': app.run()
