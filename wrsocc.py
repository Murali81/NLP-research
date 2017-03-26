# -*- coding: utf-8 -*-
fopen=open("Wordswithfreq.txt")
data=fopen.read()
fopen.close()
strg=""
for ch in data:
    strg=strg+ch
lines=strg.split("\n")
i=0
dic={}
for line in lines:
    if i%2==0:
        try:
            #print "Murali Manohar inTry"
            dic[line]=int(lines[i+1])
        except:break
    i=i+1
    #print "value of i is ",i
ls=[]
for key,val in dic.items():
    ls.append((val,key))
ls.sort(reverse=True)
strgl=""
fhand=open("wordswithhf.txt","w+")
for val,key in ls:
    print key,val
    strgl=strgl+key+" - "+str(val)+"\n"

    #fhand.write()
fhand.write(strgl)
fhand.close()

#for key in dic.values():
#    print key
