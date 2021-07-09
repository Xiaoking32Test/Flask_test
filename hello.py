from flask import Flask
from flask import make_response, redirect, abort

# 创建flask程序实例
app = Flask(__name__)

@app.route('/')
def index():
	return redirect("http://xiaoking32.top")

@app.route('/<name>')
def welcome(name):
	response = make_response("<h1>哈哈，欢迎来到xiaoking32的flask程序！</h1>")
	response.set_cookie('user', name)
	return response

@app.route('/user/<userid>')
def get_userid(userid):
	if not userid:
		abort(404)
	return "<h1>欢迎来到xiaoking32的网站！</h1>"



if __name__ == '__main__':
	app.run(debug=True)