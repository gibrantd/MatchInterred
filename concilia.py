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
fileTotalPath = "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxTotal.txt"
fileExistKey = "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxOk.txt"
print(infecha)
##
arrayExist = []
arrayTotla = []


with open(fileTotalPath) as fe:
 line = fe.readline()
 arrayTotla.append(line[:-1])
 while line:
  line = fe.readline()
  arrayTotla.append(line[:-1])
fe.close

with open(fileExistKey) as ft:
 line = ft.readline()
 arrayExist.append(line[:-1])
 while line:
  line = ft.readline()
  arrayExist.append(line[:-1])
ft.close



#print(arrayId)
print(str(len(arrayExist))+"..."+str(len(arrayTotla)))



arrayErr = []
arrayErr = list(set(arrayTotla) - set(arrayExist))

#for x in range(1, 100000):
#   arrayId.append(ObjectId('5c9d2df1dd0c0c6279a5f00c'))  
   #print(arrayId)
   #cont += 1
#fo.close
#fo = open(fileExistKey, "a")
#fo.write(str(list(collection.find({ "_id": { "$in": arrayId } },{"_id": 1}))).replace(",","\n").replace(" {'_id': '","").replace("'}","").replace("[{'_id': '","").replace("]","").replace("[","") )
#fo.write("\n")    
#fo.write(str(  list(collection.find( {'_id': ObjectId('5c9d29acdd0c0c627996adcc')}))  ) +"\n")  
#fo.write(str(list(collection.find({},{'_id':1}).limit(1000000))).replace(",","\n").replace("{'_id': ObjectId('","").replace("')}","").replace("[","").replace(" ","") )
#fo.close

finfecha = datetime.datetime.now()
print(finfecha - infecha)


