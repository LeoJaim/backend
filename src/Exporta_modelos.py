#from fileinput import close
#from multiprocessing.sharedctypes import Value
#from tarfile import PAX_NAME_FIELDS
from typing import Collection
import datetime
import pymongo
import json
import pandas as pd
import os as os
#import numpy as np

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["CollectionManager"]
mycol = mydb["staticModelCars"]
mydb.__format__ = "json"

# Consulto todas los modelos sin el campo _id
mydoc = mycol.find({}, {"_id": 0}).sort("Title", pymongo.ASCENDING)

# cuento los modelos
cantModel = myclient["CollectionManager"].staticModelCars.count_documents({})

# Armo el nombre del archivo
nomFile = "staticModels" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")

#Limpio la pantalla
os.system('cls' if os.name == 'nt' else 'clear')

# Abro el archivo json para escribir
with open("./json/" + nomFile + ".json", 'a') as json_file:
    json_file.write("[\n")
    numRow = 0
    # recorro la colección de modelos y genero el archivo json
    for x in mydoc:
        json.dump(x, json_file, indent=4, ensure_ascii=True)
        if numRow < (cantModel-1):
            json_file.write(",\n")
        numRow += 1
    json_file.write("]\n")
    print("Se escribio el archivo json " + nomFile +
          ".json" + " con " + str(cantModel) + " modelos")
    json_file.close()

modSinprecio = 0

nomFilef = "staticModels" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + \
    "_clean"
with open("./json/" + nomFilef + ".json", 'a') as json_file_final:
    json_file_final.write("[\n")
    with open("./json/" + nomFile + ".json", 'r') as json_file:
        json_data = json.load(json_file)

        for i in range(len(json_data)):
            # Trato Valores numericos
            if (json_data[i].get("Estimated Value") and json_data[i].get("Purchase Price")):
                print(json_data[i].get("Title")+" " + json_data[i].get(
                    "Estimated Value") + " " + json_data[i].get("Purchase Price"))
                print(json_data[i].get(
                    "Estimated Value").replace("\u00a0", ""))
                print(json_data[i].get("Purchase Price").replace("\u00a0", ""))
                json_data[i]["Estimated Value"] = json_data[i].get(
                    "Estimated Value").replace("\u00a0", "")
                json_data[i]["Purchase Price"] = json_data[i].get(
                    "Purchase Price").replace("\u00a0", "")
            else:
                print(json_data[i].get(
                    "Title") + " No tiene valor/campo estimado y/o ni precio de compra")
                modSinprecio += 1
                # Tengo q preguntar si falta algun campo para que no se rompa el json
                if not(json_data[i].get("Estimated Value")):
                    json_data[i]["Estimated Value"] = "$0.00"
                else:
                    json_data[i]["Estimated Value"] = json_data[i].get(
                        "Estimated Value").replace("\u00a0", "")
                if not(json_data[i].get("Purchase Price")):
                    json_data[i]["Purchase Price"] = "$0.00"
                else:
                    json_data[i]["Purchase Price"] = json_data[i].get(
                        "Purchase Price").replace("\u00a0", "")

            # Saco apostrofes a los campos Title - Description - Model - Type of Vehicle
            #Faltra tratar el campo Series y corregir Type of Vehicle
            if (json_data[i].get("Title")):
                json_data[i]["Title"] = json_data[i].get(
                    "Title").replace("\u2019", "19")
                json_data[i]["Title"] = json_data[i].get(
                    "Title").replace("\u2018", "19")
            else:
                json_data[i]["Title"] = "No tiene titulo"
            if (json_data[i].get("Description")):
                json_data[i]["Description"] = json_data[i].get(
                    "Description").replace("\u2019", "19")
                json_data[i]["Description"] = json_data[i].get(
                    "Description").replace("\u2018", "19")
            else:
                json_data[i]["Description"] = "No tiene descripcion"
            if (json_data[i].get("Model")):
                json_data[i]["Model"] = json_data[i].get(
                    "Model").replace("\u2019", "19")
                json_data[i]["Model"] = json_data[i].get(
                    "Model").replace("\u2018", "19")
            else:
                json_data[i]["Model"] = "No tiene modelo"
            if(json_data[i].get("Type of Vehicle")):
                json_data[i]["Type of Vehicle"] = json_data[i].get(
                    "Type of Vehicle").replace("\u2019", "19")
            else:
                json_data[i]["Type of Vehicle"] = "No tiene tipo de vehiculo"

            json.dump(json_data[i], json_file_final,
                      indent=4, ensure_ascii=True)
            if i < (len(json_data)-1):
                json_file_final.write(",\n")
        json_file_final.write("]\n")
print("Cantidad de modelos sin precio estimado/de compra: " + str(modSinprecio))

modSinprecio = 0
json_file_final.close()
json_file.close()
