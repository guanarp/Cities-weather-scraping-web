"""
Escrapear(extraer) el dato de la temperatura, la velocidad del viento y direccion de alguna ciudad de interes, 
y luego imprimir esos datos con el día al que corresponde. Se puede elegir cualquier página para hacer esto.
"""
import requests
from bs4 import BeautifulSoup #librerias a usar
#se reciclo codigo del bootcamp por eso esta un poquito desordenado jeje
def linkscrap(val): #aca se scrapea los links a usar y se hace una lista de ellos para usarlos en app.py
    page = requests.get("https://www.meteored.com.py/")
    lista_links= []
    soup = BeautifulSoup(page.content, "html.parser")
    all_links = soup.find_all("a", class_="anchors")
    for index in range(0,len(all_links)):
        link = all_links[index].get("href")
        lista_links.append(link)
    return lista_links[val-1]    
    


def temp(val):    
    

    page = requests.get(val) #Request pagina de clima de asuncion
    soup = BeautifulSoup(page.content, "html.parser") #soup
    maxi = soup.find_all("span", class_="maxima changeUnitT") #Se hallan todas las maximas
    mini = soup.find_all("span", class_="minima changeUnitT") #las minimas
    vel = soup.find_all("span", class_="velocidad") #La velocidad de viento (el rango)
    ciudad = soup.find_all("h1", class_="titulo") #La ciudad que se esta analizando

    ciudadtex = ciudad[0].get_text()[10:]

    """
    Aca se dio un ejemplo del dia actual, mostrando que se imprimia correctamente el primer dato de las listas generadas
    maxitex = maxi[0].get_text() 
    minitex = mini[0].get_text()
    veltex = vel[0].get_text()

    print(ciudadtex , "", maxitex, "-", minitex , "", veltex,"\n")
    """


    #imrpimiendo las predicciones con sus dias
    from datetime import datetime,date
    dias = ["Sunday", "Monday", "Tuesday" , "Wednesday", "Thursday", "Friday", "Saturday"] #lista con nombre de los dias
    hoy = datetime.today().strftime("%A") #se formatea el dia de hoy en forma de cadena
    lista_datos=[]
    def impresion(maxima,minima,velocidad,ciudad): #se define una funcion que imprima la maxima, la minima, la velocidad del
    #viento para una ciudad dada
        contador = 0 #se usa para iniciar el conteo de dias
        
        for item in range (0,len(vel)): #se podria usar cualquiera de los otros 2 args en realidad para definir el tamanho de la lista (la ciudad no)
            if contador == 0: #preguntamos por el dia de hoy
                index = dias.index(hoy)#saco el indice para tener que dia de la semana es
            contador+=1 #para que no inicie de nuevo en hoy cuando vuelva al ciclo
            index+=1 #avanza al sgte dia
            if index == len(dias):
                index = 0 #cuando llega al ultimo dia vuelve a comenzar
            datos = {
                "Ciudad": ciudad,
                "Dia": dias[index],
                "Temp": {
                    "Max":maxima[item].get_text(),
                    "Min":minima[item].get_text()
                    },
                "Velocidad":velocidad[item].get_text()
            }
            lista_datos.append(datos) #en cada ciclo agrega los valores de diccionario a la lista que usaremos
    impresion(maxi, mini, vel, ciudadtex) #se llama a la funcion definida     
    return lista_datos #al terminar el for se retornara la lista de diccionarios para el html
          
   
        
