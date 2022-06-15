from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Pass in a tutor name
    # We insert it to the html with jinja2 templates!
    return '<h1> Go to /tutor/name </h1>'


@app.route('/tutor/<name>')
def tutor_name(name):
    letters = list(name)
    tut_dict = {'tut_name': name}
    return render_template('01-Template-Variables.html',
                           name=name, mylist=letters, mydict=tut_dict)


if __name__ == '__main__':
    app.run(debug=True)
