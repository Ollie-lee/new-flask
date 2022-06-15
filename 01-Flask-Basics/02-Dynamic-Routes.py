from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello JiangRen!</h1>'

@app.route('/information')
def info():
    return '<h1>JiangRen info</h1>'

@app.route('/tutor/<name>')
def tutor(name):
    # Page for an individual puppy.
    return '<h1>This is a page for {}<h1>'.format(name)

if __name__ == '__main__':
    app.run()
