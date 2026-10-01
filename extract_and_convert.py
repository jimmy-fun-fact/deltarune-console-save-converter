#!/usr/bin/python3
import json
import os
import shutil
from time import sleep
import deltasaveutil
import io

original=os.path.abspath(input("Drop your console deltarune.sav here!\n").replace('"',''))
if not os.path.exists(original):
    exit('Path not found')

if not os.path.isdir(original):
    outdir=original+"-PC"
    with open(original,'r') as raw:
        files=json.loads(raw.read().replace('\0','')) 
        #For some reason Deltarune.sav on PS4 has a NUL at the end, and json.load() freaks out when you do that.
    if os.path.exists(outdir): shutil.rmtree(outdir)
    os.mkdir(outdir)

    for filename in files.keys():
        print("Processing "+filename)
        with open(filename,'w') as newfile:
            newfile.write(files[filename].replace('\r\n','\n'))
        if "ch" in filename:
            deltasaveutil.convert(filename)
        os.rename(os.path.join('.',filename),os.path.join(outdir,filename))
    print("\nDone!, files placed at "+outdir)
    sleep(5)
else:
    consave={}
    for filename in os.listdir(original):
        if "ch" in filename:
            with io.StringIO() as filer:
                deltasaveutil.convert(os.path.join(original,filename),direction=False,memory=True,dest=filer)
                filer.seek(0)
                consave[filename]=filer.read()
        else:
            with open(os.path.join(original,filename),'r') as filer:
                consave[filename]=filer.read()
    with open(original+"-con.sav",'w') as consavefile:
        consavefile.write(json.dumps(consave).replace('\\n','\\r\\n'))
        consavefile.write('\0')#No clue why this is here, but toby does it, so I'm doing it.
    print("\nDone!, files placed at "+original+"-con.sav")
    sleep(5)
