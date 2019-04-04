import pymongo
from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId

import sys
import time
import datetime
import pika
import os



def callback(ch, method, properties, body):                
    print(" [x] Received %r" % body)
    process_file(body)        



def process_file(body): 

    connectionOutputResFile = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.environ.get('HOSTNAME'), port=5672,
                credentials=pika.PlainCredentials(username='prosa', password='prosa')          
            )
        )
    channelOutputResFile = connectionOutputResFile.channel()
    channelOutputResFile.queue_declare(queue="PROSA-RES")

    file=str(body).replace("'","").replace("binterr","interr")    

    fileLog =  "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/logs/process.log"        
    log = open(fileLog, "a")
    log.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%s")+" INFO - Iniciando Consulta Match para el archivo: "+file+" \n")
    log.close() 
    init = datetime.datetime.now()
    
    filepath='/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/key/'+file 
    fileExistKey = "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxOk.txt"
    client = MongoClient("mongodb://"+os.environ.get('HOSTNAME')+":27017/prosa")
    db=client.prosa
    collection = db.test

    cont=0
    arrayId = []

    with open(filepath) as f:
        line = f.readline()
        arrayId.append(line[:-1])
        while line:
                cont += 1
                line = f.readline()
                arrayId.append(line[:-1])
    f.close  
    
    fileLog =  "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/logs/process.log"        
    log = open(fileLog, "a")
    log.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%s")+" INFO - Por procesar "+str(len(arrayId))+" registros Consulta Match para el archivo: "+file+" \n")
    log.close() 
    


    fo = open(fileExistKey, "a")
    fo.write("\n")    
    fo.write(str(list(collection.find({ "_id": { "$in": arrayId } },{"_id": 1}))).replace(",","\n").replace(" {'_id': '","").replace("'}","").replace("[{'_id': '","").replace("]","").replace("[","") )  
    fo.close

    channelOutputResFile.basic_publish(exchange='', routing_key='PROSA-RES', body=file)    

    connectionOutputResFile.close()          
        
    end = datetime.datetime.now()    
    log = open(fileLog, "a")
    log.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%s")+" INFO - Terminando Consulta Match para el archivo: "+file+" tomó "+str(end - init )+" \n") 
    log.close() 


if __name__ == '__main__':
    
    for arg in sys.argv[1:]:
        file = arg        
    
    connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.environ.get('HOSTNAME'), port=5672,
                credentials=pika.PlainCredentials(username='prosa', password='prosa')          
            )
        )
    channel = connection.channel()       
    channel.queue_declare(queue='PROSA-KEY')    
    channel.basic_consume(callback,
                      queue='PROSA-KEY',
                      no_ack=True)       

    channel.start_consuming()
    #process_file(file)     