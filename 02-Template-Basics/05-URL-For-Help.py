from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def indexPage():
    return render_template('05-Home.html')

@app.route('/tutor/<name>')
def tut_name(name):
    return render_template('05-Tutor.html',name=name)



if __name__ == '__main__':
    app.run(debug=True)
