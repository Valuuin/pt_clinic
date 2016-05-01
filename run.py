from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'THIS IS A POST TO GITHUB, SHOULD UPDATE ON HEROKU'
if __name__ == '__main__':
	app.run()