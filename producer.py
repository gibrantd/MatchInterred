from os import listdir 
import codecs
import datetime
import os,fnmatch
import csv
import sys


def process_file(file):     
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
  
if __name__ == '__main__':
    for arg in sys.argv[1:]:
        file = arg    
    fileOutPath =  "/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/logs/process.log"         
    f = open(fileOutPath, "a")
    print(arg)    
    f.write(arg +"\n")           
    init = datetime.datetime.now()
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%s")+"\n")             
    process_file(file)     
    end = datetime.datetime.now()    
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%s")+"\n")            
    f.write(str(end - init )+"\n")
    