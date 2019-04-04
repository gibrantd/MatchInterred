from os import listdir 
import codecs
import datetime
import os,fnmatch
import csv
import sys



if __name__ == '__main__':
    for arg in sys.argv[1:]:
        file = arg    
    init = datetime.datetime.now()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%s"))    
    os.system("split -l 100000 /Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/tef/"+file +" "+ file.replace(".txt",""))    
    end = datetime.datetime.now() 
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%s"))
    print(end - init )  
    