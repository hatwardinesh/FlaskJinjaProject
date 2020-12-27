from flask import Flask,request
from flask import render_template


app = Flask(__name__)

@app.route('/<name>')
def HelloJinja(name):
    return render_template('Welcome.html', name=name)

@app.route('/uploader', methods=['GET', 'POST'])
def UploadFile():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename != '':
            f.save(f.filename)
            myfile=open(f.filename,"r")
            data = myfile.read()
            words = data.split()        
            myfile.close()    
            return str(len(words))
        else:
            return "Upload some file"

        


if __name__ =='__main__':
    app.run(host='0.0.0.0', port='8080')    
