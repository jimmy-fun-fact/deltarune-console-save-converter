#!/usr/bin/python3
from io import BytesIO,StringIO
import struct
hell=Exception

# Copied from decompiled gml_GlobalScript_scr_saveprocess
# Should be better than what I had before.

def loadsave(file, version=2, is_console=False):
    dglobals={}
    if version==1:
        dglobals['truename']=file.readline().replace("\n","")
        if is_console:
            dglobals['othername']=deserializedata(file.readline().replace("\n",""))
        else:
            dglobals['othername']=[]
            for i in range(6):
                dglobals['othername'].append(file.readline().replace("\n",""))
        dglobals['char']=[]
        dglobals['char'].append(file.readline().replace("\n",""))
        dglobals['char'].append(file.readline().replace("\n",""))
        dglobals['char'].append(file.readline().replace("\n",""))
        dglobals['gold']=(file.readline().replace("\n",""))
        dglobals['xp']=(file.readline().replace("\n",""))
        dglobals['lv']=(file.readline().replace("\n",""))
        dglobals['inv']=(file.readline().replace("\n",""))
        dglobals['invc']=(file.readline().replace("\n",""))
        dglobals['darkzone']=(file.readline().replace("\n",""))
        dglobals['hp']=[]
        dglobals['maxhp']=[]
        dglobals['at']=[]
        dglobals['df']=[]
        dglobals['mag']=[]
        dglobals['guts']=[]
        dglobals['charweapon']=[]
        dglobals['chararmor1']=[]
        dglobals['chararmor2']=[]
        dglobals['weaponstyle']=[]
        dglobals['itemat']=[]
        dglobals['itemdf']=[]
        dglobals['itemmag']=[]
        dglobals['itembolts']=[]
        dglobals['itemgrazeamt']=[]
        dglobals['itemgrazesize']=[]
        dglobals['itemboltspeed']=[]
        dglobals['itemspecial']=[]
        dglobals['spell']=[]
        if is_console:
            dglobals['hp']=deserializedata(file.readline().replace("\n",""))
            dglobals['maxhp']=deserializedata(file.readline().replace("\n",""))
            dglobals['at']=deserializedata(file.readline().replace("\n",""))
            dglobals['df']=deserializedata(file.readline().replace("\n",""))
            dglobals['mag']=deserializedata(file.readline().replace("\n",""))
            dglobals['guts']=deserializedata(file.readline().replace("\n",""))
            dglobals['charweapon']=deserializedata(file.readline().replace("\n",""))
            dglobals['chararmor1']=deserializedata(file.readline().replace("\n",""))
            dglobals['chararmor2']=deserializedata(file.readline().replace("\n",""))
            dglobals['weaponstyle']=deserializedata(file.readline().replace("\n",""))
        
        for i in range(4):
            if not is_console:
                dglobals['hp'].append(file.readline().replace("\n",""))
                dglobals['maxhp'].append(file.readline().replace("\n",""))
                dglobals['at'].append(file.readline().replace("\n",""))
                dglobals['df'].append(file.readline().replace("\n",""))
                dglobals['mag'].append(file.readline().replace("\n",""))
                dglobals['guts'].append(file.readline().replace("\n",""))
                dglobals['charweapon'].append(file.readline().replace("\n",""))
                dglobals['chararmor1'].append(file.readline().replace("\n",""))
                dglobals['chararmor2'].append(file.readline().replace("\n",""))
                dglobals['weaponstyle'].append(file.readline().replace("\n",""))
            dglobals['itemat'].append([])
            dglobals['itemdf'].append([])
            dglobals['itemmag'].append([])
            dglobals['itembolts'].append([])
            dglobals['itemgrazeamt'].append([])
            dglobals['itemgrazesize'].append([])
            dglobals['itemboltspeed'].append([])
            dglobals['itemspecial'].append([])
            for q in range(4):
                dglobals['itemat'][i].append(file.readline().replace("\n",""))
                dglobals['itemdf'][i].append(file.readline().replace("\n",""))
                dglobals['itemmag'][i].append(file.readline().replace("\n",""))
                dglobals['itembolts'][i].append(file.readline().replace("\n",""))
                dglobals['itemgrazeamt'][i].append(file.readline().replace("\n",""))
                dglobals['itemgrazesize'][i].append(file.readline().replace("\n",""))
                dglobals['itemboltspeed'][i].append(file.readline().replace("\n",""))
                dglobals['itemspecial'][i].append(file.readline().replace("\n",""))
            dglobals['spell'].append([])
            for j in range(12):
                dglobals['spell'][i].append(file.readline().replace("\n",""))
        dglobals['boltspeed']=file.readline().replace("\n","")
        dglobals['grazeamt']=file.readline().replace("\n","")
        dglobals['grazesize']=file.readline().replace("\n","")
        if is_console:
            dglobals['item']=deserializedata(file.readline().replace("\n",""))
            dglobals['keyitem']=deserializedata(file.readline().replace("\n",""))
            dglobals['weapon']=deserializedata(file.readline().replace("\n",""))
            dglobals['armor']=deserializedata(file.readline().replace("\n",""))
        else:
            dglobals['item']=[]
            dglobals['keyitem']=[]
            dglobals['weapon']=[]
            dglobals['armor']=[]
            for j in range(13):
                dglobals['item'].append(file.readline().replace("\n",""))
                dglobals['keyitem'].append(file.readline().replace("\n",""))
                dglobals['weapon'].append(file.readline().replace("\n",""))
                dglobals['armor'].append(file.readline().replace("\n",""))
        dglobals['tension']=file.readline().replace("\n","")
        dglobals['maxtension']=file.readline().replace("\n","")
        dglobals['lweapon']=file.readline().replace("\n","")
        dglobals['larmor']=file.readline().replace("\n","")
        dglobals['lxp']=file.readline().replace("\n","")
        dglobals['llv']=file.readline().replace("\n","")
        dglobals['lgold']=file.readline().replace("\n","")
        dglobals['lhp']=file.readline().replace("\n","")
        dglobals['lmaxhp']=file.readline().replace("\n","")
        dglobals['lat']=file.readline().replace("\n","")
        dglobals['ldf']=file.readline().replace("\n","")
        dglobals['lwstrength']=file.readline().replace("\n","")
        dglobals['ladef']=file.readline().replace("\n","")
        if is_console:
            dglobals['litem']=deserializedata(file.readline().replace("\n",""))
            dglobals['phone']=deserializedata(file.readline().replace("\n",""))
            dglobals['flag']=deserializedata(file.readline().replace("\n",""))
        else:
            dglobals['litem']=[]
            dglobals['phone']=[]
            dglobals['flag']=[]
            for i in range(8):
                dglobals['litem'].append(file.readline().replace("\n",""))
                dglobals['phone'].append(file.readline().replace("\n",""))
            for i in range(9999):
                dglobals['flag'].append(file.readline().replace("\n",""))
        
        dglobals['plot']=file.readline().replace("\n","")
        dglobals['currentroom']=file.readline().replace("\n","")
        dglobals['time']=file.readline().replace("\n","")
    else:
        dglobals['truename']=file.readline().replace("\n","")
        if is_console:
            dglobals['othername']=deserializedata(file.readline().replace("\n",""))
        else:
            dglobals['othername']=[]
            for i in range(6):
                dglobals['othername'].append(file.readline().replace("\n",""))
        dglobals['char']=[]
        dglobals['char'].append(file.readline().replace("\n",""))
        dglobals['char'].append(file.readline().replace("\n",""))
        dglobals['char'].append(file.readline().replace("\n",""))
        dglobals['gold']=(file.readline().replace("\n",""))
        dglobals['xp']=(file.readline().replace("\n",""))
        dglobals['lv']=(file.readline().replace("\n",""))
        dglobals['inv']=(file.readline().replace("\n",""))
        dglobals['invc']=(file.readline().replace("\n",""))
        dglobals['darkzone']=(file.readline().replace("\n",""))
        dglobals['hp']=[]
        dglobals['maxhp']=[]
        dglobals['at']=[]
        dglobals['df']=[]
        dglobals['mag']=[]
        dglobals['guts']=[]
        dglobals['charweapon']=[]
        dglobals['chararmor1']=[]
        dglobals['chararmor2']=[]
        dglobals['weaponstyle']=[]
        dglobals['itemat']=[]
        dglobals['itemdf']=[]
        dglobals['itemmag']=[]
        dglobals['itembolts']=[]
        dglobals['itemgrazeamt']=[]
        dglobals['itemgrazesize']=[]
        dglobals['itemboltspeed']=[]
        dglobals['itemspecial']=[]
        dglobals['itemelement']=[]
        dglobals['itemelementamount']=[]
        dglobals['spell']=[]
        if is_console:
            dglobals['hp']=deserializedata(file.readline().replace("\n",""))
            dglobals['maxhp']=deserializedata(file.readline().replace("\n",""))
            dglobals['at']=deserializedata(file.readline().replace("\n",""))
            dglobals['df']=deserializedata(file.readline().replace("\n",""))
            dglobals['mag']=deserializedata(file.readline().replace("\n",""))
            dglobals['guts']=deserializedata(file.readline().replace("\n",""))
            dglobals['charweapon']=deserializedata(file.readline().replace("\n",""))
            dglobals['chararmor1']=deserializedata(file.readline().replace("\n",""))
            dglobals['chararmor2']=deserializedata(file.readline().replace("\n",""))
            dglobals['weaponstyle']=deserializedata(file.readline().replace("\n",""))
        for i in range(5):
            if not is_console:
                dglobals['hp'].append(file.readline().replace("\n",""))
                dglobals['maxhp'].append(file.readline().replace("\n",""))
                dglobals['at'].append(file.readline().replace("\n",""))
                dglobals['df'].append(file.readline().replace("\n",""))
                dglobals['mag'].append(file.readline().replace("\n",""))
                dglobals['guts'].append(file.readline().replace("\n",""))
                dglobals['charweapon'].append(file.readline().replace("\n",""))
                dglobals['chararmor1'].append(file.readline().replace("\n",""))
                dglobals['chararmor2'].append(file.readline().replace("\n",""))
                dglobals['weaponstyle'].append(file.readline().replace("\n",""))
            dglobals['itemat'].append([])
            dglobals['itemdf'].append([])
            dglobals['itemmag'].append([])
            dglobals['itembolts'].append([])
            dglobals['itemgrazeamt'].append([])
            dglobals['itemgrazesize'].append([])
            dglobals['itemboltspeed'].append([])
            dglobals['itemspecial'].append([])
            dglobals['itemelement'].append([])
            dglobals['itemelementamount'].append([])
            for q in range(4):
                dglobals['itemat'][i].append(file.readline().replace("\n",""))
                dglobals['itemdf'][i].append(file.readline().replace("\n",""))
                dglobals['itemmag'][i].append(file.readline().replace("\n",""))
                dglobals['itembolts'][i].append(file.readline().replace("\n",""))
                dglobals['itemgrazeamt'][i].append(file.readline().replace("\n",""))
                dglobals['itemgrazesize'][i].append(file.readline().replace("\n",""))
                dglobals['itemboltspeed'][i].append(file.readline().replace("\n",""))
                dglobals['itemspecial'][i].append(file.readline().replace("\n",""))
                dglobals['itemelement'][i].append(file.readline().replace("\n",""))
                dglobals['itemelementamount'][i].append(file.readline().replace("\n",""))
            dglobals['spell'].append([])
            for j in range(12):
                dglobals['spell'][i].append(file.readline().replace("\n",""))
        dglobals['boltspeed']=file.readline().replace("\n","")
        dglobals['grazeamt']=file.readline().replace("\n","")
        dglobals['grazesize']=file.readline().replace("\n","")
        if is_console:
            dglobals['item']=deserializedata(file.readline().replace("\n",""))
            dglobals['keyitem']=deserializedata(file.readline().replace("\n",""))
            dglobals['weapon']=deserializedata(file.readline().replace("\n",""))
            dglobals['armor']=deserializedata(file.readline().replace("\n",""))
            dglobals['pocketitem']=deserializedata(file.readline().replace("\n",""))
        else:
            dglobals['item']=[]
            dglobals['keyitem']=[]
            dglobals['weapon']=[]
            dglobals['armor']=[]
            dglobals['pocketitem']=[]
            for j in range(13):
                dglobals['item'].append(file.readline().replace("\n",""))
                dglobals['keyitem'].append(file.readline().replace("\n",""))
            for j in range(48):
                dglobals['weapon'].append(file.readline().replace("\n",""))
                dglobals['armor'].append(file.readline().replace("\n",""))
            for j in range(72):
                dglobals['pocketitem'].append(file.readline().replace("\n",""))
        dglobals['tension']=file.readline().replace("\n","")
        dglobals['maxtension']=file.readline().replace("\n","")
        dglobals['lweapon']=file.readline().replace("\n","")
        dglobals['larmor']=file.readline().replace("\n","")
        dglobals['lxp']=file.readline().replace("\n","")
        dglobals['llv']=file.readline().replace("\n","")
        dglobals['lgold']=file.readline().replace("\n","")
        dglobals['lhp']=file.readline().replace("\n","")
        dglobals['lmaxhp']=file.readline().replace("\n","")
        dglobals['lat']=file.readline().replace("\n","")
        dglobals['ldf']=file.readline().replace("\n","")
        dglobals['lwstrength']=file.readline().replace("\n","")
        dglobals['ladef']=file.readline().replace("\n","")
        if is_console:
            dglobals['litem']=deserializedata(file.readline().replace("\n",""))
            dglobals['phone']=deserializedata(file.readline().replace("\n",""))
            dglobals['flag']=deserializedata(file.readline().replace("\n",""))
        else:
            dglobals['litem']=[]
            dglobals['phone']=[]
            dglobals['flag']=[]
            for i in range(8):
                dglobals['litem'].append(file.readline().replace("\n",""))
                dglobals['phone'].append(file.readline().replace("\n",""))
            for i in range(2500):
                dglobals['flag'].append(file.readline().replace("\n",""))
        
        dglobals['plot']=file.readline().replace("\n","")
        dglobals['currentroom']=file.readline().replace("\n","")
        dglobals['time']=file.readline().replace("\n","")
    return dglobals
    
def savesave(file, dglobals, version=2, is_console=False):
    if version==1:
        file.write(dglobals['truename']+'\n')
        if is_console:
            file.write(serializedata(dglobals['othername'])+'\n')
        else:
            for i in range(6):
                file.write(str(dglobals['othername'][i])+'\n')
        file.write(str(dglobals['char'][0])+'\n')
        file.write(str(dglobals['char'][1])+'\n')
        file.write(str(dglobals['char'][2])+'\n')
        file.write(str(dglobals['gold'])+'\n')
        file.write(str(dglobals['xp'])+'\n')
        file.write(str(dglobals['lv'])+'\n')
        file.write(str(dglobals['inv'])+'\n')
        file.write(str(dglobals['invc'])+'\n')
        file.write(str(dglobals['darkzone'])+'\n')
        if is_console:
            file.write(serializedata(dglobals['hp'])+'\n')
            file.write(serializedata(dglobals['maxhp'])+'\n')
            file.write(serializedata(dglobals['at'])+'\n')
            file.write(serializedata(dglobals['df'])+'\n')
            file.write(serializedata(dglobals['mag'])+'\n')
            file.write(serializedata(dglobals['guts'])+'\n')
            file.write(serializedata(dglobals['charweapon'])+'\n')
            file.write(serializedata(dglobals['chararmor1'])+'\n')
            file.write(serializedata(dglobals['chararmor2'])+'\n')
            file.write(serializedata(dglobals['weaponstyle'])+'\n')
        for i in range(4):
            if not is_console:
                file.write(str(dglobals['hp'][i])+'\n')
                file.write(str(dglobals['maxhp'][i])+'\n')
                file.write(str(dglobals['at'][i])+'\n')
                file.write(str(dglobals['df'][i])+'\n')
                file.write(str(dglobals['mag'][i])+'\n')
                file.write(str(dglobals['guts'][i])+'\n')
                file.write(str(dglobals['charweapon'][i])+'\n')
                file.write(str(dglobals['chararmor1'][i])+'\n')
                file.write(str(dglobals['chararmor2'][i])+'\n')
                file.write(str(dglobals['weaponstyle'][i])+'\n')
            for q in range(4):
                file.write(str(dglobals['itemat'][i][q])+'\n')
                file.write(str(dglobals['itemdf'][i][q])+'\n')
                file.write(str(dglobals['itemmag'][i][q])+'\n')
                file.write(str(dglobals['itembolts'][i][q])+'\n')
                file.write(str(dglobals['itemgrazeamt'][i][q])+'\n')
                file.write(str(dglobals['itemgrazesize'][i][q])+'\n')
                file.write(str(dglobals['itemboltspeed'][i][q])+'\n')
                file.write(str(dglobals['itemspecial'][i][q])+'\n')
            for j in range(12):
                file.write(str(dglobals['spell'][i][j])+'\n')
        file.write(str(dglobals['boltspeed'])+'\n')
        file.write(str(dglobals['grazeamt'])+'\n')
        file.write(str(dglobals['grazesize'])+'\n')
        if is_console:
            file.write(serializedata(dglobals['item'])+'\n')
            file.write(serializedata(dglobals['keyitem'])+'\n')
            file.write(serializedata(dglobals['weapon'])+'\n')
            file.write(serializedata(dglobals['armor'])+'\n')
        else:
            for j in range(13):
                file.write(str(dglobals['item'][j])+'\n')
                file.write(str(dglobals['keyitem'][j])+'\n')
                file.write(str(dglobals['weapon'][j])+'\n')
                file.write(str(dglobals['armor'][j])+'\n')
        file.write(str(dglobals['tension'])+'\n')
        file.write(str(dglobals['maxtension'])+'\n')
        file.write(str(dglobals['lweapon'])+'\n')
        file.write(str(dglobals['larmor'])+'\n')
        file.write(str(dglobals['lxp'])+'\n')
        file.write(str(dglobals['llv'])+'\n')
        file.write(str(dglobals['lgold'])+'\n')
        file.write(str(dglobals['lhp'])+'\n')
        file.write(str(dglobals['lmaxhp'])+'\n')
        file.write(str(dglobals['lat'])+'\n')
        file.write(str(dglobals['ldf'])+'\n')
        file.write(str(dglobals['lwstrength'])+'\n')
        file.write(str(dglobals['ladef'])+'\n')
        if is_console:
            file.write(serializedata(dglobals['litem'])+'\n')
            file.write(serializedata(dglobals['phone'])+'\n')
            file.write(serializedata(dglobals['flag'])+'\n')
        else:
            for i in range(8):
                file.write(str(dglobals['litem'][i])+'\n')
                file.write(str(dglobals['phone'][i])+'\n')
            for i in range(9999):
                file.write(str(dglobals['flag'][i])+'\n')
        file.write(str(dglobals['plot'])+'\n')
        file.write(str(dglobals['currentroom'])+'\n')
        file.write(str(dglobals['time']))
    else:
        file.write(dglobals['truename']+'\n')
        if is_console:
            file.write(serializedata(dglobals['othername'])+'\n')
        else:
            for i in range(6):
                file.write(str(dglobals['othername'][i])+'\n')
        file.write(str(dglobals['char'][0])+'\n')
        file.write(str(dglobals['char'][1])+'\n')
        file.write(str(dglobals['char'][2])+'\n')
        file.write(str(dglobals['gold'])+'\n')
        file.write(str(dglobals['xp'])+'\n')
        file.write(str(dglobals['lv'])+'\n')
        file.write(str(dglobals['inv'])+'\n')
        file.write(str(dglobals['invc'])+'\n')
        file.write(str(dglobals['darkzone'])+'\n')
        if is_console:
            file.write(serializedata(dglobals['hp'])+'\n')
            file.write(serializedata(dglobals['maxhp'])+'\n')
            file.write(serializedata(dglobals['at'])+'\n')
            file.write(serializedata(dglobals['df'])+'\n')
            file.write(serializedata(dglobals['mag'])+'\n')
            file.write(serializedata(dglobals['guts'])+'\n')
            file.write(serializedata(dglobals['charweapon'])+'\n')
            file.write(serializedata(dglobals['chararmor1'])+'\n')
            file.write(serializedata(dglobals['chararmor2'])+'\n')
            file.write(serializedata(dglobals['weaponstyle'])+'\n')
        for i in range(5):
            if not is_console:
                file.write(str(dglobals['hp'][i])+'\n')
                file.write(str(dglobals['maxhp'][i])+'\n')
                file.write(str(dglobals['at'][i])+'\n')
                file.write(str(dglobals['df'][i])+'\n')
                file.write(str(dglobals['mag'][i])+'\n')
                file.write(str(dglobals['guts'][i])+'\n')
                file.write(str(dglobals['charweapon'][i])+'\n')
                file.write(str(dglobals['chararmor1'][i])+'\n')
                file.write(str(dglobals['chararmor2'][i])+'\n')
                file.write(str(dglobals['weaponstyle'][i])+'\n')
            for q in range(4):
                file.write(str(dglobals['itemat'][i][q])+'\n')
                file.write(str(dglobals['itemdf'][i][q])+'\n')
                file.write(str(dglobals['itemmag'][i][q])+'\n')
                file.write(str(dglobals['itembolts'][i][q])+'\n')
                file.write(str(dglobals['itemgrazeamt'][i][q])+'\n')
                file.write(str(dglobals['itemgrazesize'][i][q])+'\n')
                file.write(str(dglobals['itemboltspeed'][i][q])+'\n')
                file.write(str(dglobals['itemspecial'][i][q])+'\n')
                file.write(str(dglobals['itemelement'][i][q])+'\n')
                file.write(str(dglobals['itemelementamount'][i][q])+'\n')
            for j in range(12):
                file.write(str(dglobals['spell'][i][j])+'\n')
        file.write(str(dglobals['boltspeed'])+'\n')
        file.write(str(dglobals['grazeamt'])+'\n')
        file.write(str(dglobals['grazesize'])+'\n')
        if is_console:
            file.write(serializedata(dglobals['item'])+'\n')
            file.write(serializedata(dglobals['keyitem'])+'\n')
            file.write(serializedata(dglobals['weapon'])+'\n')
            file.write(serializedata(dglobals['armor'])+'\n')
            file.write(serializedata(dglobals['pocketitem'])+'\n')
        else:
            for j in range(13):
                file.write(str(dglobals['item'][j])+'\n')
                file.write(str(dglobals['keyitem'][j])+'\n')
            for j in range(48):
                file.write(str(dglobals['weapon'][j])+'\n')
                file.write(str(dglobals['armor'][j])+'\n')
            for j in range(72):
                file.write(str(dglobals['pocketitem'][j])+'\n')
        file.write(str(dglobals['tension'])+'\n')
        file.write(str(dglobals['maxtension'])+'\n')
        file.write(str(dglobals['lweapon'])+'\n')
        file.write(str(dglobals['larmor'])+'\n')
        file.write(str(dglobals['lxp'])+'\n')
        file.write(str(dglobals['llv'])+'\n')
        file.write(str(dglobals['lgold'])+'\n')
        file.write(str(dglobals['lhp'])+'\n')
        file.write(str(dglobals['lmaxhp'])+'\n')
        file.write(str(dglobals['lat'])+'\n')
        file.write(str(dglobals['ldf'])+'\n')
        file.write(str(dglobals['lwstrength'])+'\n')
        file.write(str(dglobals['ladef'])+'\n')
        if is_console:
            file.write(serializedata(dglobals['litem'])+'\n')
            file.write(serializedata(dglobals['phone'])+'\n')
            file.write(serializedata(dglobals['flag'])+'\n')
        else:
            for i in range(8):
                file.write(str(dglobals['litem'][i])+'\n')
                file.write(str(dglobals['phone'][i])+'\n')
            for i in range(2500):
                file.write(str(dglobals['flag'][i])+'\n')
        file.write(str(dglobals['plot'])+'\n')
        file.write(str(dglobals['currentroom'])+'\n')
        file.write(str(dglobals['time']))


def convert(filename, direction=True, memory=False,dest=None):
    if "ch1" in filename:   chapter=1
    else:                   chapter=2
    
    with open(filename,'r') as savefile:
        g=loadsave(savefile,chapter,is_console=direction)
    
    if memory:
        savesave(dest,g,chapter,is_console=(not direction))
    else:
        with open(filename,'w',newline='\r\n') as newsave:
            savesave(newsave,g,chapter,is_console=(not direction))

def deserializedata(daytah):
    data=BytesIO(bytearray.fromhex(daytah.replace('\n','').replace(' ','')))
    returns=[]
    magic=data.read(4) #idk if it's ever anything other than 2F010000
    # EDIT: found as 2E010000 in Switch save data
    entries=int.from_bytes(data.read(4),'little')
    for j in range(entries):
        datatype=int.from_bytes(data.read(4),'little')
        
        if datatype==1: #String, probably
            datalength=int.from_bytes(data.read(4),'little')
            datas=data.read(datalength)
            if datas==b'Normal':
                returns.append(0) #Tenna editor doesn't like my Normal, this is a hack
            else:
                returns.append(datas.decode('ascii',errors='replace'))
        
        elif datatype==0: #Double
            datas=data.read(8)
            realdata=round(struct.unpack('d',datas)[0],3)
            if round(realdata)==realdata:realdata=round(realdata)
            returns.append(realdata)
        
        elif datatype==13: #Also Double? Maybe Bool? Only seen 0 or 1 on flag 25
            datas=data.read(8)
            returns.append(struct.unpack('d',datas)[0])
        
        elif datatype==10: #Some type of int, idk. Shows up a lot in ch5
            datas=data.read(8)
            returns.append(struct.unpack('q',datas)[0])
        
        else:
            print("Unknown datatype "+str(datatype)+".")
            print("Assuming length 8 with data "+data.read(8).hex()+" at position "+str(j)+".")
            returns.append(0)
    data.close()
    return returns

def serializedata(daytah,hint=None):
    bleh=b'\x2F\x01\x00\x00'#Ignoring that 2E010000, don't know what that's about
    bleh+=struct.pack('l',len(daytah))
    hints={}
    if hint in hints.keys():
        pass #Decide later
    else:
        for j in daytah:
            try:
                if str(float(j))==j:
                    j=float(j)
                elif str(int(j))==j:
                    j=int(j)
            except ValueError:pass
            if j==0 or j=="0": #what if it's 
                bleh+=struct.pack('l',0)
                bleh+=struct.pack('d',0)
            elif type(j)==str:
                bleh+=struct.pack('l',1)
                real=j.encode('ascii',errors='replace')
                leg=len(real)
                bleh+=struct.pack('l',leg)
                bleh+=real
            elif type(j)==bytes:
                bleh+=struct.pack('l',1)
                leg=len(j)
                bleh+=struct.pack('l',leg)
                bleh+=j
            elif type(j)==int:
                bleh+=struct.pack('l',10)
                bleh+=struct.pack('q',j)
            elif type(j)==float:
                bleh+=struct.pack('l',0)
                bleh+=struct.pack('d',j)
            else:
                raise hell #panikk!
    return bleh.hex().upper()

if __name__ == "__main__":
    print("You're running the wrong script!!")
