from os import listdir 
import codecs
import datetime
import os,fnmatch
import csv
import sys
import pika
import time



def callback(ch, method, properties, body):                
    print(" [x] Received %r" % body)
    process_file(body)    
    #print(response.content)
    #print(" [x] Done")

def process_file(body): 


    connectionOutputKeyFile = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.environ.get('HOSTNAME'), port=5672,
                credentials=pika.PlainCredentials(username='prosa', password='prosa')          
            )
        )
    channelOutputKeyFile = connectionOutputKeyFile.channel()
    channelOutputKeyFile.queue_declare(queue="PROSA-KEY")

    file=str(body).replace("'","").replace("binterr","interr")    

    fileLog =  "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/logs/process.log"        
    log = open(fileLog, "a")
    log.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%s")+" INFO - Iniciando Generador de Llave para el archivo: "+file+" \n")
    log.close() 
    init = datetime.datetime.now()
    
    filepath='/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/init/'+file 
    filekey='/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/key/'+file+".txt"    
    cnt = 0   
    with open(filepath) as fp:                 
        line = fp.readline()
        cnt = 1
        k = open(filekey, "a")
        while line:                    
            key = line[0:12]+line[34:43]+line[73:77]  
            k.write(key.replace(" ","")+"\n")                                         
            #Escribe en la queue cada key                                      
            line = fp.readline()  
            if line.strip() != "":
                cnt += 1      
        print(cnt)           

    channelOutputKeyFile.basic_publish(exchange='', routing_key='PROSA-KEY', body=file+".txt")                 
    connectionOutputKeyFile.close()          
    
    
    end = datetime.datetime.now()    
    log = open(fileLog, "a")
    log.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%s")+" INFO - Terminando de Generador Llave para el archivo: "+file+" tomó "+str(end - init )+" \n") 
    log.close() 

                         
  #interred0-chunkaa
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
    channel.queue_declare(queue='PROSA-CHUNK')    
    channel.basic_consume(callback,
                      queue='PROSA-CHUNK',
                      no_ack=True)       

    channel.start_consuming()

    #process_file(file)     

    