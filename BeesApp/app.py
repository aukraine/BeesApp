from flask import Flask, render_template
from database import DB


app = Flask(__name__)

@app.route("/")
def main():
    # return 'Welcome in BeesApp!'
    return render_template('home.html')

@app.route("/hives/")
def hives():

    DB.init()
    hives = DB.find('hives')
    return render_template('hives.html', hives=hives)

if __name__ == "__main__":
    app.run(debug=True)
