import pymongo
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
fileOutPath = "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/key/"+file
fileExistKey = "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxOk.txt"

#change the MongoClient connection string to your MongoDB database instance
client = MongoClient('mongodb://localhost:27017/prosa')

db=client.prosa
collection = db.test

cont=0
arrayId = []
print(infecha)
##

with open(fileOutPath) as f:
 line = f.readline()
 arrayId.append(line[:-1])
 while line:
  cont += 1
  line = f.readline()
  arrayId.append(line[:-1])
f.close

#print(arrayId)
print(cont)
print(len(arrayId))

#for x in range(1, 100000):
#   arrayId.append(ObjectId('5c9d2df1dd0c0c6279a5f00c'))  
   #print(arrayId)
   #cont += 1
#fo.close
fo = open(fileExistKey, "a")
fo.write("\n")    
fo.write(str(list(collection.find({ "_id": { "$in": arrayId } },{"_id": 1}))).replace(",","\n").replace(" {'_id': '","").replace("'}","").replace("[{'_id': '","").replace("]","").replace("[","") )
#fo.write(str(  list(collection.find( {'_id': ObjectId('5c9d29acdd0c0c627996adcc')}))  ) +"\n")  
#fo.write(str(list(collection.find({},{'_id':1}).limit(1000000))).replace(",","\n").replace("{'_id': ObjectId('","").replace("')}","").replace("[","").replace(" ","") )
fo.close

finfecha = datetime.datetime.now()
print(finfecha - infecha)


