from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    """This function is called when user visits homepage.
    It returns string, that opens in browser.
    """
    return 'Hello Pyladies!'

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>/')
def profile(username):
    return 'User {}'.format(username)

@app.route('/url/')
def show_url():
    return url_for('profile', username='pylady')

if __name__ == "__main__":
    #opens app
    app.run()