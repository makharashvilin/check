from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<name>')
def thirdpage(name):
    return render_template("thirdpage.html",my_name=name)



if __name__ == '__main__':
    app.run(debug=True)