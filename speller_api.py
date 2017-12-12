import requests as r
import json
import sys
file_p=sys.argv[1:]
word_count=0
incorrect_words=0
fi=open(file_p[0],"r")
report=open(file_p[0]+"_report.txt","w");
for i in fi.read().split(" "):
    if i!="":
        word_count+=1
    if len(i)!=1:
            response = r.get("http://api.pearson.com/v2/dictionaries/entries?headword="+i)
            json_response=json.loads(response.text)
            if len(json_response["results"])!=0:
                report.write(i+" ")
            else:
                incorrect_words+=1
                report.write("*"+i+"* ")
    else:
        report.write(i+" ")
        
print("Total words: ",word_count)
print("Total incorrect words: ",incorrect_words)
