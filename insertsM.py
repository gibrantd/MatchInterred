from pymongo import MongoClient
#include pprint for readabillity of the 
import pprint
from bson.objectid import ObjectId

import sys
import time
import datetime



for arg in sys.argv[1:]:
 file = arg

infecha = datetime.datetime.now()
#change the MongoClient connection string to your MongoDB database instance
client = MongoClient('mongodb://localhost:27017/prosa')
db=client.prosa

 

collection = db.match
cont=0
arrayId = []
arrayNo = []
#print(infecha)

fileOutPath =  "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/logs/insertsM.log"  
f = open(fileOutPath, "a")
print("Inicio:---"+str(infecha)+"..."+file) 
  



filepath="/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/key/"+file

with open(filepath) as f:
 line = f.readline()
 while line:  
   collection.insert({'_id': line.replace("\n","")})
   cont += 1
   line = f.readline()
f.close







finfecha = datetime.datetime.now()
print(finfecha - infecha)
print("Fin:---"+str(finfecha-infecha)+"..."+file+"..."+str(cont)) 
#print(cont) 

