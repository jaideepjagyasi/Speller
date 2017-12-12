import sys
import json
file_p=sys.argv[1:]
word_count=0
print(file_p)
fi=open(file_p[0],"r")
report=open(file_p[0]+"_report.txt","w");

words=json.load(dictionary)
for i in fi.read().split(" "):
    print (i)    
    word_count+=1
    if len(i)!=1:
        try:
            if(words[i]==1):
                report.write(i+" ")
            #print(i,file=report)
            
        except:
            
            report.write("*"+i+"* ")
        #print("*"+i+"*",file=report)
    else:
        report.write(i+" ")
        
print(word_count)
