import os
import xml.etree.ElementTree as ET
import re;
from bs4 import BeautifulSoup
#outfile=open('/home/mano/Desktop/Python-m/NLP/Raw_NEW/Nepali WSD Research - Done/Instances - Nepali/Nepali  files - TDIL/Nepali Corpus - tdil - xml files/')
outfile=open("/home/mano/Desktop/Python-m/NLP/Raw_NEW/Nepali WSD Research - Done/Instances - Nepali/Nepali  files - TDIL/United.txt","w+")
#outfile = open("C:\Users\Student\Desktop\abc.txt","w+")
docs = os.listdir(".")
temp = ""

for i in range(len(docs)):
#     fileloc = workdir+ "/" + docs[i]
    # f = open(fileloc,"r")
    #parse xml
    if docs[i]=="ConvertToOne.py":continue
    fh=open(docs[i])
    strg=fh.read()
    soup=BeautifulSoup(strg,"html5lib")
    tag=soup.find('text')
    for l in tag:
        #print l
        temp=l+temp
    # temp += f.read()
    # f.close()

#print temp
outfile.write(temp.encode('utf8'))
outfile.close()
#strg=fh.read();
#body=re.findall(".*",strg)
#print body
