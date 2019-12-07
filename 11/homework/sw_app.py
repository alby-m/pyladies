from flask import Flask, abort, render_template, url_for
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return '''
    Welcome!
    This website will guide you through Star Wars universe.
    <p><a href='''+url_for('character', sw='robot')+'''>Start</a> with first character</p>
    '''

@app.route('/<sw>')
def character(sw):
    with open('sw.txt') as json_file:
        data = json.load(json_file)
    if sw in data:
        return 'Character {} belongs to the {} and his/her strong skills include {}.'.format(
            data[sw]['name'], 
            data[sw]['enlistment'], 
            ', '.join(data[sw]['strong_skills'])
        )+'''
        <p><a href='''+url_for('character', sw=data[sw]["previous"])+'''>Previous character</a></p>
        <p><a href='''+url_for('character', sw=data[sw]["next"])+'''>Next character</a></p>
        <p><a href='''+url_for('index')+'''>Return to home page</a></p>
        '''
    else:
        abort(404)

@app.errorhandler(404) 
def not_found(e):   
    return render_template('sw.html', title = '404'), 404

if __name__ == "__main__":
    #opens app
    app.run()


