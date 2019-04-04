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
collection = db.test
cont=0
arrayId = []
arrayNo = []
print(infecha)

filepath="/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/key/"+file
fileresOk="/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxOk.txt"
fileresErr="/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxErr.txt"

fOk = open(fileresOk, "a")
fErr = open(fileresErr, "a")

with open(filepath) as f:
 line = f.readline()
 while line:
  res = collection.find({"_id": line[:-1]})
  if res.count() > 0:   
   arrayId.append(line)
   fOk.write(line)
  else:   
   arrayNo.append(line)  
   fErr.write(line)
  cont += 1
  line = f.readline()
f.close


#fOk = open(fileresOk, "a")
#fOk.write(str(  list(arrayId))  )
fOk.close
#fErr = open(fileresErr, "a")
#fErr.write("\n"+str(  list(arrayNo)).replace(",","\n").replace("\\n","").replace("'","").replace("]","").replace("[","").replace(" ",""))
fErr.close


finfecha = datetime.datetime.now()
print(finfecha - infecha)
print(cont) 

