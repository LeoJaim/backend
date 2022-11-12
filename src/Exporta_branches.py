import pymongo
import json


#mydb = myclient["CollectionManager"]
#mycol = mydb["Categories"]
#input_category = int(input("Enter a category: "))
#myquery = { "_id": input_category }
#print(myquery)
#mydoc= mycol.find(myquery)
#myBranch = {
#  "name": "Barracas",
#  "address": "",
#  "#employee": 35,
#  "Revenue": 315000,
#  "Products": [
#    "CDROM",
#    "Keyboard",
#    "Mouse",
#    "Monitor",
#    "Printer",
#    "Scanner",
#    "Speaker",
#    "UPS",
#    "Video Card",
#    "Webcam"
#  ]
#}

#Inserto una nueva sucursal
#mydb.branch.insert_one(myBranch)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["webstore"]
mycol = mydb["branch"]

#Consulto todas las sucursales sin el campo _id
mydoc = mycol.find({},{"openingDate":0,"_id":0}).sort("name", pymongo.ASCENDING)

#cuento las sucursales
cantBranch = myclient["webstore"].branch.count_documents({})
#Solicito el nombre del archivo
nomFile = input("Ingrese el nombre del archivo: ")

#abro el archivo json para escribir
with open("./json/"+ nomFile + ".json", 'a') as json_file:
    json_file.write("[\n")
    numRow=0
    #recorro todas las sucursales y las escribo en el archivo json
    for x in mydoc:
         json.dump(x, json_file, indent=4)
         if numRow < (cantBranch-1):
             json_file.write(",\n")
             numRow += 1
         #else:
             #json_file.write("]")
         #imprimo en pantalla para ver el resultado
         print(x)
    json_file.write("]\n")    
    print("Se escribio el archivo json")