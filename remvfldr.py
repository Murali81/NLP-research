# -*- coding: utf-8 -*-
import shutil,os
dirls=os.listdir("Nouns2")
for fil in dirls:
    filenames=os.listdir("Nouns2/"+fil)
    for fils in filenames:
        if fils.startswith("ContextSenses"):
            #print "Murali Manohar InFiles"
            strf=str(fils)
            os.remove("Nouns2/"+fil+"/"+strf)
#shutil.rmtree('/folder_name')
