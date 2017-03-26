import os
docs = os.listdir(".")
temp = ""
outfile=open("/home/mano/Desktop/Python-m/NLP/Raw_NEW/Nepali WSD Research - Done/Instances - Nepali/Nepali  files - TDIL/UnitedForNotePadFiles.txt","w+")
temp=""
for i in range(len(docs)):
    if docs[i].endswith("py"):continue
    fh=open(docs[i])
    strg=fh.read()
    temp=strg+temp
outfile.write(temp)
outfile.close()
