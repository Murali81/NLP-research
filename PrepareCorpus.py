# -*- coding: utf-8 -*-
import sys,re,os,urllib,time,random
from bs4 import BeautifulSoup
from collections import Counter
workdir = "./Senses/Nouns3"
suff=open("./Senses/suffixes.txt","a")
with open("./merged.txt", "r") as f:
    myfile = open("./ps.txt","r")
    wordcsv = myfile.read()
    wordlist = wordcsv.split(",")
    myfile.close()
    text = f.read()
    text = text.replace("\n","").replace("\r","")
print "Searching..."
def cleanse(s):
    k = s.split(" ")
    k = filter(None, k)
    string = ""
    for word in k:
        string = string + " " + word
    return string
def get_trans(word):
    try:
        url='http://www.shabdkosh.com/te/translate?e='+word+'&l=te'
        link1 = urllib.urlopen(url)
        data = link1.read()
        soup = BeautifulSoup(data,"html5lib")
        tags=soup('span')
        for tag in tags:
        	if tag.get("class") is None :continue
        	stg=tag.get("class")
        	stg=str(stg[0])
        	if stg=="in":
                	num=re.findall(".*",tag.text)
                    #print("Murali Manohar REgex InTransliteration")
                	if len(num)>0:
                    		return str(num[0])
    except:
        print("Check your internet connection.I'll wait for 2 minutes")
        time.sleep(120)
    return "undefined"               #This is when the return above is not done
def create_files(word,senses):
    for i in range(senses):
        k = i+1;
        c = open(workdir+"/"+word+"_"+get_trans(word)+"/"+"ContextSenses00"+str(k)+".txt","w+");c.close()
        i = open(workdir+"/"+word+"_"+get_trans(word)+"/"+"Instances00"+str(k)+".txt","w+");i.close()
    n = open(workdir+"/"+word+"_"+get_trans(word)+"/"+"No_of_Senses.txt","w+");n.write(str(senses));n.close()
    return
def create_sense(word,syn,gloss,example,engtr):
    for i in range(len(syn)):
        temp = ""
        k = i+1
        temp = temp + syn[i] + " -"
        temp = temp + gloss[i] + "      "
        temp = temp + '"' + example[i] + '"'
        temp = temp + "\n" + engtr[i]
        #print len(engtr)
        c = open(workdir+"/"+word+"_"+get_trans(word)+"/"+"Senses00"+str(k)+".txt","w+");c.write(temp.encode('utf8'));c.close()
    return
def get_sge(word):
	try:
		flst = []
		lst1=list()
		lst2=list()
	    	lst4=list()
		lst3=list()
		url="http://tdil-dc.in/indowordnet/first?langno=15&queryword="+word
		link=urllib.urlopen(url)
		data=link.read()
		soup=BeautifulSoup(data,"html5lib")
		tags=soup('span')
		labels=soup('label')
		for labe in labels:
			text1=""
			text2=""
			text3=""
			text4=""
			if labe.get("id")=="words":
				strg=labe.text
				text1=text1+strg.replace(" ","").replace("\n","")
				lst1.append(text1)
			if labe.get("id")=="gloss":
				strg=labe.text
				text2=text2+strg.replace("\n","");text2 = cleanse(text2)
				lst2.append(text2)
			if labe.get("id")=="ex_stmt":
				strg=labe.text
				strg2=(strg.replace("\n","").replace("&#034;","")).split('"')
				text3=text3+strg2[1]
				lst3.append(text3)
			if labe.get("id")=="gloss_eng":
			    strg=labe.text
			    text4=text4+strg.replace("\n","")
			    text4=cleanse(text4)
			    lst4.append(text4)
		flst.append(lst1)
		flst.append(lst2)
		flst.append(lst3)
		flst.append(lst4)
		return flst
	except:
		print("Check your internet connection.Will wait for 2 mins")
        #print("Murali Manohar Except block get_sge")
		time.sleep(120)
notfound = open(workdir+"/notfound.txt","a")

def amputate(st):           #This makes sure that the extracted paragraph does not start from the middle of a sentence
    txts=""
    o = open(st)
    dats=o.read()
    paras=dats.split("\n\n\n\n\n")
    #print(len(dats))
    for line in paras[:-1]:
        pos=line.find(". ")
        #print(pos)
        #print(line[pos+2:])
        txts=txts+"<I>"+line[pos+2:]+"\n\n\n\n\n"
    #print(txts)
    #print("Murali Manohar Here in amp")
    o.close()
    o=open(st,"w+")
    o.write(txts)
    o.close()

#amputate()

for word in wordlist:
    temp = ""
    search = word
    counter = -1
    body = text.split(" ")
    occ_indices = []
    for item in body:
        counter +=1
        if not item.startswith(search):continue
        find=re.findall(search+'\S*',item)
        if len(find)>0:
            strg1=find[0]
            trgword=strg1.split(search)
            suff.write(trgword[1]+"\n")
            occ_indices.append(counter)         # It notes the position for every occurance of a single word
    counter = len(occ_indices)
    if counter < 2:
        notf = word+"\n"
        notfound.write(notf)
        continue
    else:
        if not os.path.exists(workdir+"/"+word+"_"+get_trans(word)):
            os.makedirs(workdir+"/"+word+"_"+get_trans(word))
        o = open(workdir+"/"+word+"_"+get_trans(word)+"/"+"Context.txt","w+")
        contextloc=workdir+"/"+word+"_"+get_trans(word)+"/"+"Context.txt"
        tw = open(workdir+"/"+word+"_"+get_trans(word)+"/"+"targetword.txt","w+")
        print(word)
        print(len(occ_indices))
        tw.write(word)
        tw.close()
        #replace this
        final = get_sge(word)
        create_files(word,len(final[0]))
        create_sense(word,final[0],final[1],final[2],final[3])
        # occr=0
        for ind in occ_indices:
            # occr=occr+1
            # if occr==1000:break
            for x in range(ind-35,ind+35):
                if x == ind:
                    temp = temp + body[ind] + " = sense "
                else:
                    temp = temp + body[x] + " "
            temp += "</I>\n\n\n\n\n<I>"
            #print("Murali Manohar InMainNewLines")
        o.write("<I>"+temp[:-3])
        o.close()
        #print("Wrote")
        amputate(contextloc)
        #print("End of word")
 # time.sleep(20)
notfound.close()
suff.close()
