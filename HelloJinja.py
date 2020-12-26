from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/<name>')
def HelloJinja(name):
    return render_template('Welcome.html', name=name)


if __name__ =='__main__':
    app.run(host='0.0.0.0', port='8080')    
