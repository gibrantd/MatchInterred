import codecs
import sys
import os

def main(args):
    command="ls -lrt tef/* | grep interred | awk -F\" \" '{print $9}' | awk -F\".\" '{print $1}' | awk '{print \"mv \"$1\".generating \"$1\".txt\"}' | sh"
    for i in range(int(args[0])):     
     name="/Users/interware/Documents/IW/PROSA/Match-Interredes/Lab/tef/interred%d." % (i) 
     f= codecs.open(name+"generating","w+", "utf-8")   
     for j in range(int(args[1])):
         f.write("%d-" % (i+1))
         f.write("%d   HH201407171E  CTIP3  BZ    000000181286779000000001812867790000000018128677900000000\n" % (j+1))         
     f.close()     
    #print(command) 
    os.system(command)   
   
if __name__== "__main__":
  args=[]
  for arg in sys.argv[1:]:
        args.append(arg)
  main(args)


