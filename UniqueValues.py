from flask import Flask, request
from flask import render_template
from collections import OrderedDict

app = Flask(__name__)

@app.route('/' )
def renderUploadPage():
    return  render_template('UploadFile.html')

@app.route('/upload', methods = ['GET','POST'])
def returnUniqueRecords():
    if request.method =='POST':
        f = request.files['file']  
        if f.filename != '':
            print("try below")
            f.save('UploadedFiles/'+ f.filename)
            myFile = open('UploadedFiles/'+ f.filename,'r')
            data = myFile.read()
            words = data.split()
            myFile.close()
            words = list(OrderedDict.fromkeys(words))
            return str(words)
        else:
            return "Please upload file"



if __name__ == '__main__':
    #app.config['DEBUG']=True
    app.run(host='0.0.0.0', port='8080')            