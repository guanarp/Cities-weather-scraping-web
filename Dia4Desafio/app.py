#hoy creamos una pagina web (local) con un flask
from flask import Flask,render_template
import temp
app= Flask(__name__) #crea el objeto app, instancia la clase flask, el parametro __name__ indica que esta en el "script principal"

val = {
    1:"https://www.meteored.com.py/tiempo-en_Asuncion-America+Sur-Paraguay-Central--1-22742.html",
    2:"https://www.meteored.com.py/tiempo-en_Ciudad+del+Este-America+Sur-Paraguay-Alto+Parana--1-22739.html",
    3:"https://www.meteored.com.py/tiempo-en_Santa+Rita-America+Sur-Paraguay-Alto+Parana--1-22732.html",
    4:"https://www.meteored.com.py/tiempo-en_Encarnacion-America+Sur-Paraguay-Itapua--1-22959.html",
    5:"https://www.meteored.com.py/tiempo-en_Pedro+Juan+Caballero-America+Sur-Paraguay-Amambay--1-22839.html",
    6:"https://www.meteored.com.py/tiempo-en_Caaguazu-America+Sur-Paraguay-Caaguazu--1-22926.html",
    7:"https://www.meteored.com.py/tiempo-en_J+E+Estigarribia-America+Sur-Paraguay-Caaguazu--1-22766.html",
    8:"https://www.meteored.com.py/tiempo-en_Santa+Rita-America+Sur-Paraguay-Alto+Parana--1-22732.html",
    9:"https://www.meteored.com.py/tiempo-en_Raul+Oviedo-America+Sur-Paraguay-Caaguazu--1-22758.html",
    10:"https://www.meteored.com.py/tiempo-en_San+Alberto-America+Sur-Paraguay-Alto+Parana--1-22713.html",
    11:"https://www.meteored.com.py/tiempo-en_Naranjal-America+Sur-Paraguay-Alto+Parana--1-22757.html",
    12:"https://www.meteored.com.py/tiempo-en_San+Lorenzo-America+Sur-Paraguay-Central--1-22745.html"
} #diccionario para las direcciones de scraping

@app.route("/") #este es el index
def indice():
    return render_template('index.html') #el indice

@app.route("/Asuncion")  #a partir de aca cada ciudad es "igual salvo que se accede a otro item del diccionario"
def Asu():
    print(val[1])
    print(temp.temp(val[1]))
    return render_template('Ciudad.html',datos = temp.temp(val[1]))

@app.route("/CDE") 
def Cde():
    return render_template('Ciudad.html',datos = temp.temp(val[2]))

@app.route("/SantaRita") 
def SR():
    return render_template('Ciudad.html',datos = temp.temp(val[3]))

@app.route("/Encarnacion") 
def Enc():
    return render_template('Ciudad.html',datos = temp.temp(val[4]))

@app.route("/PJC") 
def PJC():
    return render_template('Ciudad.html',datos = temp.temp(val[5]))

@app.route("/Caaguazu") 
def Caag():
    return render_template('Ciudad.html',datos = temp.temp(val[6]))

@app.route("/JEEstigarribia") 
def JEE():
    return render_template('Ciudad.html',datos = temp.temp(val[7]))

@app.route("/SanIsidro") 
def SI():
    return render_template('Ciudad.html', datos = temp.temp(val[8]))

@app.route("/RaulOviedo") 
def RO():
    return render_template('Ciudad.html', datos = temp.temp(val[9]))

@app.route("/SanAlberto") 
def SA():
    return render_template('Ciudad.html', datos = temp.temp(val[10]))

@app.route("/Naranjal") 
def Nan():
    return render_template('Ciudad.html', datos = temp.temp(val[11]))

@app.route("/SanLorenzo") 
def SL():
    return render_template('Ciudad.html', datos = temp.temp(val[12]))


if __name__ == "__main__":
    app.run()
    #esto se ejecuta solamente si es el archivo principal
#set FLASK_APP=app.py #(export en linux en vez de export) Se escribe esto en la terminal para agregar al path
#flask run #hace correr el servidor localmente
