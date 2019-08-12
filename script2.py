from flask import Flask

app = Flask(__name__)

@app.route('/about/')
def about():
    return "Hai the website from Liju Raju"

@app.route('/home/')
def home():
    return "Welcome to home page"


if __name__=="__main__":
    app.run(debug=True)
