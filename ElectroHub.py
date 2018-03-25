from flask import Flask,render_template

from urllib import urlencode
app = Flask(__name__)

plist = {"Gina_Valentina" : [["Title","link"],
                         ["Title2","link2"]]\
        ,"Mia_Khalifa":[["asdas","asdas"],["asdas","sdasd"]]}
@app.route('/')
@app.route('/<string:name>')
def hello_world(name=None):
    if name != None:
        print(name)
        title = name.replace(" ","%")
    else:
        title = "ElectroHub"
    return render_template("index.html",title=title,plist=plist)


if __name__ == '__main__':
    app.run(debug=True)
