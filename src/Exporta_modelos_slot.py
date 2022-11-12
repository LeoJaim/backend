from datetime import datetime
from fileinput import close
from multiprocessing.sharedctypes import Value
from typing import Collection
import datetime
import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["CollectionManager"]
mycol = mydb["slotModelCars"]
mydb.__format__ = "json"

# Consulto todas los modelos sin el campo _id
mydoc = mycol.find({}, {"_id": 0, "RutaImagen": 0, "RutaImagen2": 0}).sort(
    "Descripcion", pymongo.ASCENDING)

# cuento los modelos
cantModel = myclient["CollectionManager"].slotModelCars.count_documents({})

# Defino el nombre del archivo
nomFile = "slotModels" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# abro el archivo json para escribir
with open("./json/" + nomFile + ".json", 'a') as json_file:
    json_file.write("[\n")
    numRow = 0
    # recorro todas las sucursales y las escribo en el archivo json
    for x in mydoc:
        json.dump(x, json_file, indent=4)
        if numRow < (cantModel-1):
            json_file.write(",\n")
        numRow += 1
    json_file.write("]\n")
    print("Se escribio el archivo json " + nomFile +
          ".json" + " con " + str(cantModel) + " modelos")
    json_file.close()

modSinprecio = 0
modSinColor = 0
modSinDesc = 0
modSinDescColeccion = 0

with open("./json/" + nomFile + ".json", 'r') as json_file:
    json_data = json.load(json_file)
    #ask=input("Desea ver el contenido del archivo? (y/n): ")
    for i in range(len(json_data)):
        if (json_data[i].get("Descripcion") and json_data[i].get("Precio") and json_data[i].get("Color") and json_data[i].get("DescripcionColeccion")):
            print(json_data[i].get("Descripcion") + " " + json_data[i].get("Precio") + " " +
                  json_data[i].get("Color") + " " + json_data[i].get("DescripcionColeccion"))
        if json_data[i].get("Descripcion"): print(json_data[i].get("Descripcion"))
        else: 
            print("No tiene descripcion")
            modSinColor += 1
        if json_data[i].get("Precio"): print(json_data[i].get("Precio"))
        else: 
            print("No tiene precio")
            modSinprecio += 1
        if json_data[i].get("Color"): print(json_data[i].get("Color"))
        else: 
            print("No tiene color")
            modSinColor +=1
        if json_data[i].get("DescripcionColeccion"): print(json_data[i].get("DescripcionColeccion"))
        else: 
            print("No tiene descripcion de coleccion")
            modSinDescColeccion +=1
        #ask = input("Desea ver el siguiente registro? (y/n): ")
print("Se encontraron " + str(modSinprecio) + " modelos sin precio"+"/n" )
print("Se encontraron " + str(modSinColor) + " modelos sin color"+"/n")
print("Se encontraron " + str(modSinDescColeccion) + " modelos sin descripcion de coleccion"+"/n")
print("Se encontraron " + str(modSinDesc) + " modelos sin descripcion")
json_file.close()
