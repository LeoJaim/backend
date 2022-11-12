from fileinput import close
from multiprocessing.sharedctypes import Value
from sqlite3 import SQLITE_INSERT
from typing import Collection
import datetime
import pymongo
import json
import mysql.connector

# conexión a la base de datos MONGODB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# conexión a la base de datos MYSQL
mydbsql = mysql.connector.connect(
    host="localhost", user="root", passwd="Minolta10*", database="Colman")

# defino el cursor para la base de datos MYSQL
mycursor = mydbsql.cursor()

#Todavia no funciona
# defino el instert para la base de datos MYSQL
sqlinsert = "INSERT INTO staticModelCars (modelname, modeldescription, year ,model, estimatedvalue, purchasevalue , condition) VALUES (%s, %s, %s,%s, %s, %s, %s)"

# array de datos para el insert de la base de datos MYSQL
val = ()

# elijo la base de datos de MONGODB y la colección de datos
mydb = myclient["CollectionManager"]
mycol = mydb["staticModelCars"]
mydb.__format__ = "json"

# Consulto todas los modelos sin el campo _id
mydoc = mycol.find({}, {"_id": 0}).sort("Title", pymongo.ASCENDING)

# cuento los modelos
cantModel = myclient["CollectionManager"].staticModelCars.count_documents({})

# Armo el nombre del archivo
nomFile = "staticModels" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Abro el archivo json para escribir
with open("./json/" + nomFile + ".json", 'a') as json_file:
    json_file.write("[\n")
    numRow = 0
    # recorro todos los registros y las escribo en el archivo json
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
    "_final"
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
            # Faltra tratar el campo Series y corregir Type of Vehicle
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

            # inserto en tabla de BBDD MYSQL
            val = ('"' + json_data[i].get("Title").replace("'", "") + '"' + "," + '"' + json_data[i].get("Description").replace("'", "") + '"' + "," + '"' + json_data[i].get("year") + '"' + "," + '"' + json_data[i].get("Model").replace("'", "") + '"' + "," + '"' + json_data[i].get(
                "Type of Vehicle").replace("'", "") + '"' + "," + '"' + json_data[i].get("Estimated Value").replace("'$", "") + '"' + "," + '"' + json_data[i].get("Purchase Price").replace("'$", "") + '"')
            print(val)
            pp = input("NADA:")
            mycursor.execute(sqlinsert, val)
        if i < (len(json_data)-1):
            json_file_final.write(",\n")
        json_file_final.write("]\n")
print("Cantidad de modelos sin precio estimado/de compra: " + str(modSinprecio))

modSinprecio = 0
mydbsql.commit()
json_file_final.close()
json_file.close()
