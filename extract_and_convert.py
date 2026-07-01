#!/usr/bin/python3
import json
import os
import shutil
from time import sleep
import deltasaveutil

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
    input("Conversion to console not yet supported.")
    consave={}
    for filename in os.listdir(original):
        if "ch" in filename:
            pass#handle this
        else:
            with open(os.path.join(original,filename),'r') as filer:
                consave[filename]=filer.read()
    with open('Deltarune-con.sav','w') as consavefile:
        consavefile.write(json.dumps(consave))
        consavefile.write('\0')#No clue why this is here, but toby does it, so I'm doing it.
    