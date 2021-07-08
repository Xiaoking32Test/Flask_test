from flask import Flask

# 创建flask程序实例
app = Flask(__name__)

@app.route('/<name>/<int:age>')
def index(name, age):
	return "<h1>哈哈，欢迎%d岁的%s来到xiaoking32的flask程序！</h1>" % (age, name)

if __name__ == '__main__':
	app.run(debug=True)