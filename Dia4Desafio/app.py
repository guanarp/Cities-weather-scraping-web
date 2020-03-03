#hoy creamos una pagina web (local) con un flask
from flask import Flask,render_template
import temp
app= Flask(__name__) #crea el objeto app, instancia la clase flask, el parametro __name__ indica que esta en el "script principal"


@app.route("/") #este es el index
def indice():
    return render_template('index.html') #el indice

@app.route("/Asuncion")  #a partir de aca cada ciudad es "igual salvo que se accede a otro item del diccionario"
def Asu():
    return render_template('Ciudad.html',datos = temp.temp( temp.linkscrap(1) ) )

@app.route("/CDE") 
def Cde():
    return render_template('Ciudad.html',datos = temp.temp(temp.linkscrap(2)))

@app.route("/SantaRita") 
def SR():
    return render_template('Ciudad.html',datos = temp.temp(temp.linkscrap(3)))

@app.route("/Encarnacion") 
def Enc():
    return render_template('Ciudad.html',datos = temp.temp(temp.linkscrap(4)))

@app.route("/PJC") 
def PJC():
    return render_template('Ciudad.html',datos = temp.temp(temp.linkscrap(5)))

@app.route("/Caaguazu") 
def Caag():
    return render_template('Ciudad.html',datos = temp.temp(temp.linkscrap(6)))

@app.route("/JEEstigarribia") 
def JEE():
    return render_template('Ciudad.html',datos = temp.temp(temp.linkscrap(7)))

@app.route("/SanIsidro") 
def SI():
    return render_template('Ciudad.html', datos = temp.temp(temp.linkscrap(8)))

@app.route("/RaulOviedo") 
def RO():
    return render_template('Ciudad.html', datos = temp.temp(temp.linkscrap(9)))

@app.route("/SanAlberto") 
def SA():
    return render_template('Ciudad.html', datos = temp.temp(temp.linkscrap(10)))

@app.route("/Naranjal") 
def Nan():
    return render_template('Ciudad.html', datos = temp.temp(temp.linkscrap(11)))

@app.route("/SanLorenzo") 
def SL():
    return render_template('Ciudad.html', datos = temp.temp(temp.linkscrap(12)))


if __name__ == "__main__":
    app.run()
    #esto se ejecuta solamente si es el archivo principal
#set FLASK_APP=app.py #(export en linux en vez de export) Se escribe esto en la terminal para agregar al path
#flask run #hace correr el servidor localmente
