from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    tutors = ['jiang', 'ren']
    return render_template('03-Template-Control-Flow.html',
                           tutors=tutors)


if __name__ == '__main__':
    app.run(debug=True)
