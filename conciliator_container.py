import pymongo
from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId

import os
import sys
import time
import datetime
import pika
import subprocess
from subprocess import PIPE, Popen



def callback(ch, method, properties, body):                
    print(" [x] Received %r" % body)
    process_file(body)        



def process_file(body): 
    file=str(body).replace("'","").replace("binterr","interr")    

    fileLog =  "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/logs/process.log"        
    log = open(fileLog, "a")
    log.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%s")+" INFO - Iniciando Conciliación del archivo: "+file+" \n")
    log.close() 
    init = datetime.datetime.now()
    
    filepath='/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/key/'+file 
    fileOk = "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxOk.txt"
    fileErrorKey = "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/done/trxError.txt"
    
    
    command="bash /PROSA/Lab/diff-command.sh "+fileOk+" "+filepath+" "+fileErrorKey
    
    p=subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    (output,err) = p.communicate()
    print(output)
    print(err)

    #print(command)
    #os.system(command)
    
    end = datetime.datetime.now()    
    log = open(fileLog, "a")
    #log.write(str(output)+" \n") 
    #log.write(str(err)+" \n") 
    log.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%s")+" INFO - Terminando Conciliación del archivo: "+file+" tomó "+str(end - init )+" \n") 
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
    channel.queue_declare(queue='PROSA-RES')    
    channel.basic_consume(callback,
                      queue='PROSA-RES',
                      no_ack=True)       

    channel.start_consuming()
    #process_file(file)     