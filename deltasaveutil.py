#!/usr/bin/python3
from io import BytesIO
from fractions import Fraction
import struct

savefilemapch1="""001: global.truename
002: global.othername
003: global.char[0]
004: global.char[1]
005: global.char[2]
006: global.gold
007: global.xp
008: global.lv
009: global.inv
010: global.invc
011: global.darkzone
012: global.hp
013: global.maxhp
014: global.at
015: global.df
016: global.mag
017: global.guts
018: global.charweapon
019: global.chararmor1
020: global.chararmor2
021: global.weaponstyle
022: global.itemat[0, 0]
023: global.itemdf[0, 0]
024: global.itemmag[0, 0]
025: global.itembolts[0, 0]
026: global.itemgrazeamt[0, 0]
027: global.itemgrazesize[0, 0]
028: global.itemboltspeed[0, 0]
029: global.itemspecial[0, 0]
030: global.itemat[0, 1]
031: global.itemdf[0, 1]
032: global.itemmag[0, 1]
033: global.itembolts[0, 1]
034: global.itemgrazeamt[0, 1]
035: global.itemgrazesize[0, 1]
036: global.itemboltspeed[0, 1]
037: global.itemspecial[0, 1]
038: global.itemat[0, 2]
039: global.itemdf[0, 2]
040: global.itemmag[0, 2]
041: global.itembolts[0, 2]
042: global.itemgrazeamt[0, 2]
043: global.itemgrazesize[0, 2]
044: global.itemboltspeed[0, 2]
045: global.itemspecial[0, 2]
046: global.itemat[0, 3]
047: global.itemdf[0, 3]
048: global.itemmag[0, 3]
049: global.itembolts[0, 3]
050: global.itemgrazeamt[0, 3]
051: global.itemgrazesize[0, 3]
052: global.itemboltspeed[0, 3]
053: global.itemspecial[0, 3]
054: global.spell[0, 0]
055: global.spell[0, 1]
056: global.spell[0, 2]
057: global.spell[0, 3]
058: global.spell[0, 4]
059: global.spell[0, 5]
060: global.spell[0, 6]
061: global.spell[0, 7]
062: global.spell[0, 8]
063: global.spell[0, 9]
064: global.spell[0, 10]
065: global.spell[0, 11]
066: global.itemat[1, 0]
067: global.itemdf[1, 0]
068: global.itemmag[1, 0]
069: global.itembolts[1, 0]
070: global.itemgrazeamt[1, 0]
071: global.itemgrazesize[1, 0]
072: global.itemboltspeed[1, 0]
073: global.itemspecial[1, 0]
074: global.itemat[1, 1]
075: global.itemdf[1, 1]
076: global.itemmag[1, 1]
077: global.itembolts[1, 1]
078: global.itemgrazeamt[1, 1]
079: global.itemgrazesize[1, 1]
080: global.itemboltspeed[1, 1]
081: global.itemspecial[1, 1]
082: global.itemat[1, 2]
083: global.itemdf[1, 2]
084: global.itemmag[1, 2]
085: global.itembolts[1, 2]
086: global.itemgrazeamt[1, 2]
087: global.itemgrazesize[1, 2]
088: global.itemboltspeed[1, 2]
089: global.itemspecial[1, 2]
090: global.itemat[1, 3]
091: global.itemdf[1, 3]
092: global.itemmag[1, 3]
093: global.itembolts[1, 3]
094: global.itemgrazeamt[1, 3]
095: global.itemgrazesize[1, 3]
096: global.itemboltspeed[1, 3]
097: global.itemspecial[1, 3]
098: global.spell[1, 0]
099: global.spell[1, 1]
100: global.spell[1, 2]
101: global.spell[1, 3]
102: global.spell[1, 4]
103: global.spell[1, 5]
104: global.spell[1, 6]
105: global.spell[1, 7]
106: global.spell[1, 8]
107: global.spell[1, 9]
108: global.spell[1, 10]
109: global.spell[1, 11]
110: global.itemat[2, 0]
111: global.itemdf[2, 0]
112: global.itemmag[2, 0]
113: global.itembolts[2, 0]
114: global.itemgrazeamt[2, 0]
115: global.itemgrazesize[2, 0]
116: global.itemboltspeed[2, 0]
117: global.itemspecial[2, 0]
118: global.itemat[2, 1]
119: global.itemdf[2, 1]
120: global.itemmag[2, 1]
121: global.itembolts[2, 1]
122: global.itemgrazeamt[2, 1]
123: global.itemgrazesize[2, 1]
124: global.itemboltspeed[2, 1]
125: global.itemspecial[2, 1]
126: global.itemat[2, 2]
127: global.itemdf[2, 2]
128: global.itemmag[2, 2]
129: global.itembolts[2, 2]
130: global.itemgrazeamt[2, 2]
131: global.itemgrazesize[2, 2]
132: global.itemboltspeed[2, 2]
133: global.itemspecial[2, 2]
134: global.itemat[2, 3]
135: global.itemdf[2, 3]
136: global.itemmag[2, 3]
137: global.itembolts[2, 3]
138: global.itemgrazeamt[2, 3]
139: global.itemgrazesize[2, 3]
140: global.itemboltspeed[2, 3]
141: global.itemspecial[2, 3]
142: global.spell[2, 0]
143: global.spell[2, 1]
144: global.spell[2, 2]
145: global.spell[2, 3]
146: global.spell[2, 4]
147: global.spell[2, 5]
148: global.spell[2, 6]
149: global.spell[2, 7]
150: global.spell[2, 8]
151: global.spell[2, 9]
152: global.spell[2, 10]
153: global.spell[2, 11]
154: global.itemat[3, 0]
155: global.itemdf[3, 0]
156: global.itemmag[3, 0]
157: global.itembolts[3, 0]
158: global.itemgrazeamt[3, 0]
159: global.itemgrazesize[3, 0]
160: global.itemboltspeed[3, 0]
161: global.itemspecial[3, 0]
162: global.itemat[3, 1]
163: global.itemdf[3, 1]
164: global.itemmag[3, 1]
165: global.itembolts[3, 1]
166: global.itemgrazeamt[3, 1]
167: global.itemgrazesize[3, 1]
168: global.itemboltspeed[3, 1]
169: global.itemspecial[3, 1]
170: global.itemat[3, 2]
171: global.itemdf[3, 2]
172: global.itemmag[3, 2]
173: global.itembolts[3, 2]
174: global.itemgrazeamt[3, 2]
175: global.itemgrazesize[3, 2]
176: global.itemboltspeed[3, 2]
177: global.itemspecial[3, 2]
178: global.itemat[3, 3]
179: global.itemdf[3, 3]
180: global.itemmag[3, 3]
181: global.itembolts[3, 3]
182: global.itemgrazeamt[3, 3]
183: global.itemgrazesize[3, 3]
184: global.itemboltspeed[3, 3]
185: global.itemspecial[3, 3]
186: global.spell[3, 0]
187: global.spell[3, 1]
188: global.spell[3, 2]
189: global.spell[3, 3]
190: global.spell[3, 4]
191: global.spell[3, 5]
192: global.spell[3, 6]
193: global.spell[3, 7]
194: global.spell[3, 8]
195: global.spell[3, 9]
196: global.spell[3, 10]
197: global.spell[3, 11]
198: global.boltspeed
199: global.grazeamt
200: global.grazesize
201: global.item
202: global.keyitem
203: global.weapon
204: global.armor
205: global.tension
206: global.maxtension
207: global.lweapon
208: global.larmor
209: global.lxp
210: global.llv
211: global.lgold
212: global.lhp
213: global.lmaxhp
214: global.lat
215: global.ldf
216: global.lwstrength
217: global.ladef
218: global.litem
219: global.phone
220: global.flags
221: global.plot
222: global.currentroom
223: global.time""".split('\n')

savefilemapch2="""001: global.truename
002: global.othername
003: global.char[0]
004: global.char[1]
005: global.char[2]
006: global.gold
007: global.xp
008: global.lv
009: global.inv
010: global.invc
011: global.darkzone
012: global.hp
013: global.maxhp
014: global.at
015: global.df
016: global.mag
017: global.guts
018: global.charweapon
019: global.chararmor1
020: global.chararmor2
021: global.weaponstyle
022: global.itemat[0, 0]
023: global.itemdf[0, 0]
024: global.itemmag[0, 0]
025: global.itembolts[0, 0]
026: global.itemgrazeamt[0, 0]
027: global.itemgrazesize[0, 0]
028: global.itemboltspeed[0, 0]
029: global.itemspecial[0, 0]
030: global.itemelement[0, 0]
031: global.itemelementamount[0, 0]
032: global.itemat[0, 1]
033: global.itemdf[0, 1]
034: global.itemmag[0, 1]
035: global.itembolts[0, 1]
036: global.itemgrazeamt[0, 1]
037: global.itemgrazesize[0, 1]
038: global.itemboltspeed[0, 1]
039: global.itemspecial[0, 1]
040: global.itemelement[0, 1]
041: global.itemelementamount[0, 1]
042: global.itemat[0, 2]
043: global.itemdf[0, 2]
044: global.itemmag[0, 2]
045: global.itembolts[0, 2]
046: global.itemgrazeamt[0, 2]
047: global.itemgrazesize[0, 2]
048: global.itemboltspeed[0, 2]
049: global.itemspecial[0, 2]
050: global.itemelement[0, 2]
051: global.itemelementamount[0, 2]
052: global.itemat[0, 3]
053: global.itemdf[0, 3]
054: global.itemmag[0, 3]
055: global.itembolts[0, 3]
056: global.itemgrazeamt[0, 3]
057: global.itemgrazesize[0, 3]
058: global.itemboltspeed[0, 3]
059: global.itemspecial[0, 3]
060: global.itemelement[0, 3]
061: global.itemelementamount[0, 3]
062: global.spell[0, 0]
063: global.spell[0, 1]
064: global.spell[0, 2]
065: global.spell[0, 3]
066: global.spell[0, 4]
067: global.spell[0, 5]
068: global.spell[0, 6]
069: global.spell[0, 7]
070: global.spell[0, 8]
071: global.spell[0, 9]
072: global.spell[0, 10]
073: global.spell[0, 11]
074: global.itemat[1, 0]
075: global.itemdf[1, 0]
076: global.itemmag[1, 0]
077: global.itembolts[1, 0]
078: global.itemgrazeamt[1, 0]
079: global.itemgrazesize[1, 0]
080: global.itemboltspeed[1, 0]
081: global.itemspecial[1, 0]
082: global.itemelement[1, 0]
083: global.itemelementamount[1, 0]
084: global.itemat[1, 1]
085: global.itemdf[1, 1]
086: global.itemmag[1, 1]
087: global.itembolts[1, 1]
088: global.itemgrazeamt[1, 1]
089: global.itemgrazesize[1, 1]
090: global.itemboltspeed[1, 1]
091: global.itemspecial[1, 1]
092: global.itemelement[1, 1]
093: global.itemelementamount[1, 1]
094: global.itemat[1, 2]
095: global.itemdf[1, 2]
096: global.itemmag[1, 2]
097: global.itembolts[1, 2]
098: global.itemgrazeamt[1, 2]
099: global.itemgrazesize[1, 2]
100: global.itemboltspeed[1, 2]
101: global.itemspecial[1, 2]
102: global.itemelement[1, 2]
103: global.itemelementamount[1, 2]
104: global.itemat[1, 3]
105: global.itemdf[1, 3]
106: global.itemmag[1, 3]
107: global.itembolts[1, 3]
108: global.itemgrazeamt[1, 3]
109: global.itemgrazesize[1, 3]
110: global.itemboltspeed[1, 3]
111: global.itemspecial[1, 3]
112: global.itemelement[1, 3]
113: global.itemelementamount[1, 3]
114: global.spell[1, 0]
115: global.spell[1, 1]
116: global.spell[1, 2]
117: global.spell[1, 3]
118: global.spell[1, 4]
119: global.spell[1, 5]
120: global.spell[1, 6]
121: global.spell[1, 7]
122: global.spell[1, 8]
123: global.spell[1, 9]
124: global.spell[1, 10]
125: global.spell[1, 11]
126: global.itemat[2, 0]
127: global.itemdf[2, 0]
128: global.itemmag[2, 0]
129: global.itembolts[2, 0]
130: global.itemgrazeamt[2, 0]
131: global.itemgrazesize[2, 0]
132: global.itemboltspeed[2, 0]
133: global.itemspecial[2, 0]
134: global.itemelement[2, 0]
135: global.itemelementamount[2, 0]
136: global.itemat[2, 1]
137: global.itemdf[2, 1]
138: global.itemmag[2, 1]
139: global.itembolts[2, 1]
140: global.itemgrazeamt[2, 1]
141: global.itemgrazesize[2, 1]
142: global.itemboltspeed[2, 1]
143: global.itemspecial[2, 1]
144: global.itemelement[2, 1]
145: global.itemelementamount[2, 1]
146: global.itemat[2, 2]
147: global.itemdf[2, 2]
148: global.itemmag[2, 2]
149: global.itembolts[2, 2]
150: global.itemgrazeamt[2, 2]
151: global.itemgrazesize[2, 2]
152: global.itemboltspeed[2, 2]
153: global.itemspecial[2, 2]
154: global.itemelement[2, 2]
155: global.itemelementamount[2, 2]
156: global.itemat[2, 3]
157: global.itemdf[2, 3]
158: global.itemmag[2, 3]
159: global.itembolts[2, 3]
160: global.itemgrazeamt[2, 3]
161: global.itemgrazesize[2, 3]
162: global.itemboltspeed[2, 3]
163: global.itemspecial[2, 3]
164: global.itemelement[2, 3]
165: global.itemelementamount[2, 3]
166: global.spell[2, 0]
167: global.spell[2, 1]
168: global.spell[2, 2]
169: global.spell[2, 3]
170: global.spell[2, 4]
171: global.spell[2, 5]
172: global.spell[2, 6]
173: global.spell[2, 7]
174: global.spell[2, 8]
175: global.spell[2, 9]
176: global.spell[2, 10]
177: global.spell[2, 11]
178: global.itemat[3, 0]
179: global.itemdf[3, 0]
180: global.itemmag[3, 0]
181: global.itembolts[3, 0]
182: global.itemgrazeamt[3, 0]
183: global.itemgrazesize[3, 0]
184: global.itemboltspeed[3, 0]
185: global.itemspecial[3, 0]
186: global.itemelement[3, 0]
187: global.itemelementamount[3, 0]
188: global.itemat[3, 1]
189: global.itemdf[3, 1]
190: global.itemmag[3, 1]
191: global.itembolts[3, 1]
192: global.itemgrazeamt[3, 1]
193: global.itemgrazesize[3, 1]
194: global.itemboltspeed[3, 1]
195: global.itemspecial[3, 1]
196: global.itemelement[3, 1]
197: global.itemelementamount[3, 1]
198: global.itemat[3, 2]
199: global.itemdf[3, 2]
200: global.itemmag[3, 2]
201: global.itembolts[3, 2]
202: global.itemgrazeamt[3, 2]
203: global.itemgrazesize[3, 2]
204: global.itemboltspeed[3, 2]
205: global.itemspecial[3, 2]
206: global.itemelement[3, 2]
207: global.itemelementamount[3, 2]
208: global.itemat[3, 3]
209: global.itemdf[3, 3]
210: global.itemmag[3, 3]
211: global.itembolts[3, 3]
212: global.itemgrazeamt[3, 3]
213: global.itemgrazesize[3, 3]
214: global.itemboltspeed[3, 3]
215: global.itemspecial[3, 3]
216: global.itemelement[3, 3]
217: global.itemelementamount[3, 3]
218: global.spell[3, 0]
219: global.spell[3, 1]
220: global.spell[3, 2]
221: global.spell[3, 3]
222: global.spell[3, 4]
223: global.spell[3, 5]
224: global.spell[3, 6]
225: global.spell[3, 7]
226: global.spell[3, 8]
227: global.spell[3, 9]
228: global.spell[3, 10]
229: global.spell[3, 11]
230: global.itemat[4, 0]
231: global.itemdf[4, 0]
232: global.itemmag[4, 0]
233: global.itembolts[4, 0]
234: global.itemgrazeamt[4, 0]
235: global.itemgrazesize[4, 0]
236: global.itemboltspeed[4, 0]
237: global.itemspecial[4, 0]
238: global.itemelement[4, 0]
239: global.itemelementamount[4, 0]
240: global.itemat[4, 1]
241: global.itemdf[4, 1]
242: global.itemmag[4, 1]
243: global.itembolts[4, 1]
244: global.itemgrazeamt[4, 1]
245: global.itemgrazesize[4, 1]
246: global.itemboltspeed[4, 1]
247: global.itemspecial[4, 1]
248: global.itemelement[4, 1]
249: global.itemelementamount[4, 1]
250: global.itemat[4, 2]
251: global.itemdf[4, 2]
252: global.itemmag[4, 2]
253: global.itembolts[4, 2]
254: global.itemgrazeamt[4, 2]
255: global.itemgrazesize[4, 2]
256: global.itemboltspeed[4, 2]
257: global.itemspecial[4, 2]
258: global.itemelement[4, 2]
259: global.itemelementamount[4, 2]
260: global.itemat[4, 3]
261: global.itemdf[4, 3]
262: global.itemmag[4, 3]
263: global.itembolts[4, 3]
264: global.itemgrazeamt[4, 3]
265: global.itemgrazesize[4, 3]
266: global.itemboltspeed[4, 3]
267: global.itemspecial[4, 3]
268: global.itemelement[4, 3]
269: global.itemelementamount[4, 3]
270: global.spell[4, 0]
271: global.spell[4, 1]
272: global.spell[4, 2]
273: global.spell[4, 3]
274: global.spell[4, 4]
275: global.spell[4, 5]
276: global.spell[4, 6]
277: global.spell[4, 7]
278: global.spell[4, 8]
279: global.spell[4, 9]
280: global.spell[4, 10]
281: global.spell[4, 11]
282: global.boltspeed
283: global.grazeamt
284: global.grazesize
285: global.item
286: global.keyitem
287: global.weapon
288: global.armor
289: global.pocketitem
290: global.tension
291: global.maxtension
292: global.lweapon
293: global.larmor
294: global.lxp
295: global.llv
296: global.lgold
297: global.lhp
298: global.lmaxhp
299: global.lat
300: global.ldf
301: global.lwstrength
302: global.ladef
303: global.litem
304: global.phone
305: global.flags
306: global.plot
307: global.currentroom
308: global.time""".split('\n')

def convert(filename):
    saver={}
    if "ch1" in filename:
        mapper=savefilemapch1
        chapter=1
    else:
        mapper=savefilemapch2
        chapter=2
    
    with open(filename,'r') as savefile:
        g=savefile.read().split('\n')
        for a in range(len(g)):
            if g[a][:4]=='2F01' or g[a][:4]=='2E01':
                saver[mapper[a][5:]]=deserializedata(g[a])
            else:
                saver[mapper[a][5:]]=(g[a])
    
    if chapter==2:   #Chapter 2+ save
        newsave=(
            saver['global.truename']+'\n'+
            '\n'.join(saver['global.othername'])+'\n'+
            str(saver['global.char[0]'])+'\n'+
            str(saver['global.char[1]'])+'\n'+
            str(saver['global.char[2]'])+'\n'+
            str(saver['global.gold'])+'\n'+
            str(saver['global.xp'])+'\n'+
            str(saver['global.lv'])+'\n'+
            str(saver['global.inv'])+'\n'+
            str(saver['global.invc'])+'\n'+
            str(saver['global.darkzone'])+'\n'+
            str(saver['global.hp'][0])+'\n'+
            str(saver['global.maxhp'][0])+'\n'+
            str(saver['global.at'][0])+'\n'+
            str(saver['global.df'][0])+'\n'+
            str(saver['global.mag'][0])+'\n'+
            str(saver['global.guts'][0])+'\n'+
            str(saver['global.charweapon'][0])+'\n'+
            str(saver['global.chararmor1'][0])+'\n'+
            str(saver['global.chararmor2'][0])+'\n'+
            str(saver['global.weaponstyle'][0])+'\n'+
            str(saver['global.itemat[0, 0]'])+'\n'+
            str(saver['global.itemdf[0, 0]'])+'\n'+
            str(saver['global.itemmag[0, 0]'])+'\n'+
            str(saver['global.itembolts[0, 0]'])+'\n'+
            str(saver['global.itemgrazeamt[0, 0]'])+'\n'+
            str(saver['global.itemgrazesize[0, 0]'])+'\n'+
            str(saver['global.itemboltspeed[0, 0]'])+'\n'+
            str(saver['global.itemspecial[0, 0]'])+'\n'+
            str(saver['global.itemelement[0, 0]'])+'\n'+
            str(saver['global.itemelementamount[0, 0]'])+'\n'+
            str(saver['global.itemat[0, 1]'])+'\n'+
            str(saver['global.itemdf[0, 1]'])+'\n'+
            str(saver['global.itemmag[0, 1]'])+'\n'+
            str(saver['global.itembolts[0, 1]'])+'\n'+
            str(saver['global.itemgrazeamt[0, 1]'])+'\n'+
            str(saver['global.itemgrazesize[0, 1]'])+'\n'+
            str(saver['global.itemboltspeed[0, 1]'])+'\n'+
            str(saver['global.itemspecial[0, 1]'])+'\n'+
            str(saver['global.itemelement[0, 1]'])+'\n'+
            str(saver['global.itemelementamount[0, 1]'])+'\n'+
            str(saver['global.itemat[0, 2]'])+'\n'+
            str(saver['global.itemdf[0, 2]'])+'\n'+
            str(saver['global.itemmag[0, 2]'])+'\n'+
            str(saver['global.itembolts[0, 2]'])+'\n'+
            str(saver['global.itemgrazeamt[0, 2]'])+'\n'+
            str(saver['global.itemgrazesize[0, 2]'])+'\n'+
            str(saver['global.itemboltspeed[0, 2]'])+'\n'+
            str(saver['global.itemspecial[0, 2]'])+'\n'+
            str(saver['global.itemelement[0, 2]'])+'\n'+
            str(saver['global.itemelementamount[0, 2]'])+'\n'+
            str(saver['global.itemat[0, 3]'])+'\n'+
            str(saver['global.itemdf[0, 3]'])+'\n'+
            str(saver['global.itemmag[0, 3]'])+'\n'+
            str(saver['global.itembolts[0, 3]'])+'\n'+
            str(saver['global.itemgrazeamt[0, 3]'])+'\n'+
            str(saver['global.itemgrazesize[0, 3]'])+'\n'+
            str(saver['global.itemboltspeed[0, 3]'])+'\n'+
            str(saver['global.itemspecial[0, 3]'])+'\n'+
            str(saver['global.itemelement[0, 3]'])+'\n'+
            str(saver['global.itemelementamount[0, 3]'])+'\n'+
            str(saver['global.spell[0, 0]'])+'\n'+
            str(saver['global.spell[0, 1]'])+'\n'+
            str(saver['global.spell[0, 2]'])+'\n'+
            str(saver['global.spell[0, 3]'])+'\n'+
            str(saver['global.spell[0, 4]'])+'\n'+
            str(saver['global.spell[0, 5]'])+'\n'+
            str(saver['global.spell[0, 6]'])+'\n'+
            str(saver['global.spell[0, 7]'])+'\n'+
            str(saver['global.spell[0, 8]'])+'\n'+
            str(saver['global.spell[0, 9]'])+'\n'+
            str(saver['global.spell[0, 10]'])+'\n'+
            str(saver['global.spell[0, 11]'])+'\n'+
            str(saver['global.hp'][1])+'\n'+
            str(saver['global.maxhp'][1])+'\n'+
            str(saver['global.at'][1])+'\n'+
            str(saver['global.df'][1])+'\n'+
            str(saver['global.mag'][1])+'\n'+
            str(saver['global.guts'][1])+'\n'+
            str(saver['global.charweapon'][1])+'\n'+
            str(saver['global.chararmor1'][1])+'\n'+
            str(saver['global.chararmor2'][1])+'\n'+
            str(saver['global.weaponstyle'][1])+'\n'+
            str(saver['global.itemat[1, 0]'])+'\n'+
            str(saver['global.itemdf[1, 0]'])+'\n'+
            str(saver['global.itemmag[1, 0]'])+'\n'+
            str(saver['global.itembolts[1, 0]'])+'\n'+
            str(saver['global.itemgrazeamt[1, 0]'])+'\n'+
            str(saver['global.itemgrazesize[1, 0]'])+'\n'+
            str(saver['global.itemboltspeed[1, 0]'])+'\n'+
            str(saver['global.itemspecial[1, 0]'])+'\n'+
            str(saver['global.itemelement[1, 0]'])+'\n'+
            str(saver['global.itemelementamount[1, 0]'])+'\n'+
            str(saver['global.itemat[1, 1]'])+'\n'+
            str(saver['global.itemdf[1, 1]'])+'\n'+
            str(saver['global.itemmag[1, 1]'])+'\n'+
            str(saver['global.itembolts[1, 1]'])+'\n'+
            str(saver['global.itemgrazeamt[1, 1]'])+'\n'+
            str(saver['global.itemgrazesize[1, 1]'])+'\n'+
            str(saver['global.itemboltspeed[1, 1]'])+'\n'+
            str(saver['global.itemspecial[1, 1]'])+'\n'+
            str(saver['global.itemelement[1, 1]'])+'\n'+
            str(saver['global.itemelementamount[1, 1]'])+'\n'+
            str(saver['global.itemat[1, 2]'])+'\n'+
            str(saver['global.itemdf[1, 2]'])+'\n'+
            str(saver['global.itemmag[1, 2]'])+'\n'+
            str(saver['global.itembolts[1, 2]'])+'\n'+
            str(saver['global.itemgrazeamt[1, 2]'])+'\n'+
            str(saver['global.itemgrazesize[1, 2]'])+'\n'+
            str(saver['global.itemboltspeed[1, 2]'])+'\n'+
            str(saver['global.itemspecial[1, 2]'])+'\n'+
            str(saver['global.itemelement[1, 2]'])+'\n'+
            str(saver['global.itemelementamount[1, 2]'])+'\n'+
            str(saver['global.itemat[1, 3]'])+'\n'+
            str(saver['global.itemdf[1, 3]'])+'\n'+
            str(saver['global.itemmag[1, 3]'])+'\n'+
            str(saver['global.itembolts[1, 3]'])+'\n'+
            str(saver['global.itemgrazeamt[1, 3]'])+'\n'+
            str(saver['global.itemgrazesize[1, 3]'])+'\n'+
            str(saver['global.itemboltspeed[1, 3]'])+'\n'+
            str(saver['global.itemspecial[1, 3]'])+'\n'+
            str(saver['global.itemelement[1, 3]'])+'\n'+
            str(saver['global.itemelementamount[1, 3]'])+'\n'+
            str(saver['global.spell[1, 0]'])+'\n'+
            str(saver['global.spell[1, 1]'])+'\n'+
            str(saver['global.spell[1, 2]'])+'\n'+
            str(saver['global.spell[1, 3]'])+'\n'+
            str(saver['global.spell[1, 4]'])+'\n'+
            str(saver['global.spell[1, 5]'])+'\n'+
            str(saver['global.spell[1, 6]'])+'\n'+
            str(saver['global.spell[1, 7]'])+'\n'+
            str(saver['global.spell[1, 8]'])+'\n'+
            str(saver['global.spell[1, 9]'])+'\n'+
            str(saver['global.spell[1, 10]'])+'\n'+
            str(saver['global.spell[1, 11]'])+'\n'+
            str(saver['global.hp'][2])+'\n'+
            str(saver['global.maxhp'][2])+'\n'+
            str(saver['global.at'][2])+'\n'+
            str(saver['global.df'][2])+'\n'+
            str(saver['global.mag'][2])+'\n'+
            str(saver['global.guts'][2])+'\n'+
            str(saver['global.charweapon'][2])+'\n'+
            str(saver['global.chararmor1'][2])+'\n'+
            str(saver['global.chararmor2'][2])+'\n'+
            str(saver['global.weaponstyle'][2])+'\n'+
            str(saver['global.itemat[2, 0]'])+'\n'+
            str(saver['global.itemdf[2, 0]'])+'\n'+
            str(saver['global.itemmag[2, 0]'])+'\n'+
            str(saver['global.itembolts[2, 0]'])+'\n'+
            str(saver['global.itemgrazeamt[2, 0]'])+'\n'+
            str(saver['global.itemgrazesize[2, 0]'])+'\n'+
            str(saver['global.itemboltspeed[2, 0]'])+'\n'+
            str(saver['global.itemspecial[2, 0]'])+'\n'+
            str(saver['global.itemelement[2, 0]'])+'\n'+
            str(saver['global.itemelementamount[2, 0]'])+'\n'+
            str(saver['global.itemat[2, 1]'])+'\n'+
            str(saver['global.itemdf[2, 1]'])+'\n'+
            str(saver['global.itemmag[2, 1]'])+'\n'+
            str(saver['global.itembolts[2, 1]'])+'\n'+
            str(saver['global.itemgrazeamt[2, 1]'])+'\n'+
            str(saver['global.itemgrazesize[2, 1]'])+'\n'+
            str(saver['global.itemboltspeed[2, 1]'])+'\n'+
            str(saver['global.itemspecial[2, 1]'])+'\n'+
            str(saver['global.itemelement[2, 1]'])+'\n'+
            str(saver['global.itemelementamount[2, 1]'])+'\n'+
            str(saver['global.itemat[2, 2]'])+'\n'+
            str(saver['global.itemdf[2, 2]'])+'\n'+
            str(saver['global.itemmag[2, 2]'])+'\n'+
            str(saver['global.itembolts[2, 2]'])+'\n'+
            str(saver['global.itemgrazeamt[2, 2]'])+'\n'+
            str(saver['global.itemgrazesize[2, 2]'])+'\n'+
            str(saver['global.itemboltspeed[2, 2]'])+'\n'+
            str(saver['global.itemspecial[2, 2]'])+'\n'+
            str(saver['global.itemelement[2, 2]'])+'\n'+
            str(saver['global.itemelementamount[2, 2]'])+'\n'+
            str(saver['global.itemat[2, 3]'])+'\n'+
            str(saver['global.itemdf[2, 3]'])+'\n'+
            str(saver['global.itemmag[2, 3]'])+'\n'+
            str(saver['global.itembolts[2, 3]'])+'\n'+
            str(saver['global.itemgrazeamt[2, 3]'])+'\n'+
            str(saver['global.itemgrazesize[2, 3]'])+'\n'+
            str(saver['global.itemboltspeed[2, 3]'])+'\n'+
            str(saver['global.itemspecial[2, 3]'])+'\n'+
            str(saver['global.itemelement[2, 3]'])+'\n'+
            str(saver['global.itemelementamount[2, 3]'])+'\n'+
            str(saver['global.spell[2, 0]'])+'\n'+
            str(saver['global.spell[2, 1]'])+'\n'+
            str(saver['global.spell[2, 2]'])+'\n'+
            str(saver['global.spell[2, 3]'])+'\n'+
            str(saver['global.spell[2, 4]'])+'\n'+
            str(saver['global.spell[2, 5]'])+'\n'+
            str(saver['global.spell[2, 6]'])+'\n'+
            str(saver['global.spell[2, 7]'])+'\n'+
            str(saver['global.spell[2, 8]'])+'\n'+
            str(saver['global.spell[2, 9]'])+'\n'+
            str(saver['global.spell[2, 10]'])+'\n'+
            str(saver['global.spell[2, 11]'])+'\n'+
            str(saver['global.hp'][3])+'\n'+
            str(saver['global.maxhp'][3])+'\n'+
            str(saver['global.at'][3])+'\n'+
            str(saver['global.df'][3])+'\n'+
            str(saver['global.mag'][3])+'\n'+
            str(saver['global.guts'][3])+'\n'+
            str(saver['global.charweapon'][3])+'\n'+
            str(saver['global.chararmor1'][3])+'\n'+
            str(saver['global.chararmor2'][3])+'\n'+
            str(saver['global.weaponstyle'][3])+'\n'+
            str(saver['global.itemat[3, 0]'])+'\n'+
            str(saver['global.itemdf[3, 0]'])+'\n'+
            str(saver['global.itemmag[3, 0]'])+'\n'+
            str(saver['global.itembolts[3, 0]'])+'\n'+
            str(saver['global.itemgrazeamt[3, 0]'])+'\n'+
            str(saver['global.itemgrazesize[3, 0]'])+'\n'+
            str(saver['global.itemboltspeed[3, 0]'])+'\n'+
            str(saver['global.itemspecial[3, 0]'])+'\n'+
            str(saver['global.itemelement[3, 0]'])+'\n'+
            str(saver['global.itemelementamount[3, 0]'])+'\n'+
            str(saver['global.itemat[3, 1]'])+'\n'+
            str(saver['global.itemdf[3, 1]'])+'\n'+
            str(saver['global.itemmag[3, 1]'])+'\n'+
            str(saver['global.itembolts[3, 1]'])+'\n'+
            str(saver['global.itemgrazeamt[3, 1]'])+'\n'+
            str(saver['global.itemgrazesize[3, 1]'])+'\n'+
            str(saver['global.itemboltspeed[3, 1]'])+'\n'+
            str(saver['global.itemspecial[3, 1]'])+'\n'+
            str(saver['global.itemelement[3, 1]'])+'\n'+
            str(saver['global.itemelementamount[3, 1]'])+'\n'+
            str(saver['global.itemat[3, 2]'])+'\n'+
            str(saver['global.itemdf[3, 2]'])+'\n'+
            str(saver['global.itemmag[3, 2]'])+'\n'+
            str(saver['global.itembolts[3, 2]'])+'\n'+
            str(saver['global.itemgrazeamt[3, 2]'])+'\n'+
            str(saver['global.itemgrazesize[3, 2]'])+'\n'+
            str(saver['global.itemboltspeed[3, 2]'])+'\n'+
            str(saver['global.itemspecial[3, 2]'])+'\n'+
            str(saver['global.itemelement[3, 2]'])+'\n'+
            str(saver['global.itemelementamount[3, 2]'])+'\n'+
            str(saver['global.itemat[3, 3]'])+'\n'+
            str(saver['global.itemdf[3, 3]'])+'\n'+
            str(saver['global.itemmag[3, 3]'])+'\n'+
            str(saver['global.itembolts[3, 3]'])+'\n'+
            str(saver['global.itemgrazeamt[3, 3]'])+'\n'+
            str(saver['global.itemgrazesize[3, 3]'])+'\n'+
            str(saver['global.itemboltspeed[3, 3]'])+'\n'+
            str(saver['global.itemspecial[3, 3]'])+'\n'+
            str(saver['global.itemelement[3, 3]'])+'\n'+
            str(saver['global.itemelementamount[3, 3]'])+'\n'+
            str(saver['global.spell[3, 0]'])+'\n'+
            str(saver['global.spell[3, 1]'])+'\n'+
            str(saver['global.spell[3, 2]'])+'\n'+
            str(saver['global.spell[3, 3]'])+'\n'+
            str(saver['global.spell[3, 4]'])+'\n'+
            str(saver['global.spell[3, 5]'])+'\n'+
            str(saver['global.spell[3, 6]'])+'\n'+
            str(saver['global.spell[3, 7]'])+'\n'+
            str(saver['global.spell[3, 8]'])+'\n'+
            str(saver['global.spell[3, 9]'])+'\n'+
            str(saver['global.spell[3, 10]'])+'\n'+
            str(saver['global.spell[3, 11]'])+'\n'+
            str(saver['global.hp'][4])+'\n'+
            str(saver['global.maxhp'][4])+'\n'+
            str(saver['global.at'][4])+'\n'+
            str(saver['global.df'][4])+'\n'+
            str(saver['global.mag'][4])+'\n'+
            str(saver['global.guts'][4])+'\n'+
            str(saver['global.charweapon'][4])+'\n'+
            str(saver['global.chararmor1'][4])+'\n'+
            str(saver['global.chararmor2'][4])+'\n'+
            str(saver['global.weaponstyle'][4])+'\n'+
            str(saver['global.itemat[4, 0]'])+'\n'+
            str(saver['global.itemdf[4, 0]'])+'\n'+
            str(saver['global.itemmag[4, 0]'])+'\n'+
            str(saver['global.itembolts[4, 0]'])+'\n'+
            str(saver['global.itemgrazeamt[4, 0]'])+'\n'+
            str(saver['global.itemgrazesize[4, 0]'])+'\n'+
            str(saver['global.itemboltspeed[4, 0]'])+'\n'+
            str(saver['global.itemspecial[4, 0]'])+'\n'+
            str(saver['global.itemelement[4, 0]'])+'\n'+
            str(saver['global.itemelementamount[4, 0]'])+'\n'+
            str(saver['global.itemat[4, 1]'])+'\n'+
            str(saver['global.itemdf[4, 1]'])+'\n'+
            str(saver['global.itemmag[4, 1]'])+'\n'+
            str(saver['global.itembolts[4, 1]'])+'\n'+
            str(saver['global.itemgrazeamt[4, 1]'])+'\n'+
            str(saver['global.itemgrazesize[4, 1]'])+'\n'+
            str(saver['global.itemboltspeed[4, 1]'])+'\n'+
            str(saver['global.itemspecial[4, 1]'])+'\n'+
            str(saver['global.itemelement[4, 1]'])+'\n'+
            str(saver['global.itemelementamount[4, 1]'])+'\n'+
            str(saver['global.itemat[4, 2]'])+'\n'+
            str(saver['global.itemdf[4, 2]'])+'\n'+
            str(saver['global.itemmag[4, 2]'])+'\n'+
            str(saver['global.itembolts[4, 2]'])+'\n'+
            str(saver['global.itemgrazeamt[4, 2]'])+'\n'+
            str(saver['global.itemgrazesize[4, 2]'])+'\n'+
            str(saver['global.itemboltspeed[4, 2]'])+'\n'+
            str(saver['global.itemspecial[4, 2]'])+'\n'+
            str(saver['global.itemelement[4, 2]'])+'\n'+
            str(saver['global.itemelementamount[4, 2]'])+'\n'+
            str(saver['global.itemat[4, 3]'])+'\n'+
            str(saver['global.itemdf[4, 3]'])+'\n'+
            str(saver['global.itemmag[4, 3]'])+'\n'+
            str(saver['global.itembolts[4, 3]'])+'\n'+
            str(saver['global.itemgrazeamt[4, 3]'])+'\n'+
            str(saver['global.itemgrazesize[4, 3]'])+'\n'+
            str(saver['global.itemboltspeed[4, 3]'])+'\n'+
            str(saver['global.itemspecial[4, 3]'])+'\n'+
            str(saver['global.itemelement[4, 3]'])+'\n'+
            str(saver['global.itemelementamount[4, 3]'])+'\n'+
            str(saver['global.spell[4, 0]'])+'\n'+
            str(saver['global.spell[4, 1]'])+'\n'+
            str(saver['global.spell[4, 2]'])+'\n'+
            str(saver['global.spell[4, 3]'])+'\n'+
            str(saver['global.spell[4, 4]'])+'\n'+
            str(saver['global.spell[4, 5]'])+'\n'+
            str(saver['global.spell[4, 6]'])+'\n'+
            str(saver['global.spell[4, 7]'])+'\n'+
            str(saver['global.spell[4, 8]'])+'\n'+
            str(saver['global.spell[4, 9]'])+'\n'+
            str(saver['global.spell[4, 10]'])+'\n'+
            str(saver['global.spell[4, 11]'])+'\n'+
            str(saver['global.boltspeed'])+'\n'+
            str(saver['global.grazeamt'])+'\n'+
            str(saver['global.grazesize'])+'\n'+
            str(saver['global.item'][0])+'\n'+
            str(saver['global.keyitem'][0])+'\n'+
            str(saver['global.item'][1])+'\n'+
            str(saver['global.keyitem'][1])+'\n'+
            str(saver['global.item'][2])+'\n'+
            str(saver['global.keyitem'][2])+'\n'+
            str(saver['global.item'][3])+'\n'+
            str(saver['global.keyitem'][3])+'\n'+
            str(saver['global.item'][4])+'\n'+
            str(saver['global.keyitem'][4])+'\n'+
            str(saver['global.item'][5])+'\n'+
            str(saver['global.keyitem'][5])+'\n'+
            str(saver['global.item'][6])+'\n'+
            str(saver['global.keyitem'][6])+'\n'+
            str(saver['global.item'][7])+'\n'+
            str(saver['global.keyitem'][7])+'\n'+
            str(saver['global.item'][8])+'\n'+
            str(saver['global.keyitem'][8])+'\n'+
            str(saver['global.item'][9])+'\n'+
            str(saver['global.keyitem'][9])+'\n'+
            str(saver['global.item'][10])+'\n'+
            str(saver['global.keyitem'][10])+'\n'+
            str(saver['global.item'][11])+'\n'+
            str(saver['global.keyitem'][11])+'\n'+
            str(saver['global.item'][12])+'\n'+
            str(saver['global.keyitem'][12])+'\n'+
            str(saver['global.weapon'][0])+'\n'+
            str(saver['global.armor'][0])+'\n'+
            str(saver['global.weapon'][1])+'\n'+
            str(saver['global.armor'][1])+'\n'+
            str(saver['global.weapon'][2])+'\n'+
            str(saver['global.armor'][2])+'\n'+
            str(saver['global.weapon'][3])+'\n'+
            str(saver['global.armor'][3])+'\n'+
            str(saver['global.weapon'][4])+'\n'+
            str(saver['global.armor'][4])+'\n'+
            str(saver['global.weapon'][5])+'\n'+
            str(saver['global.armor'][5])+'\n'+
            str(saver['global.weapon'][6])+'\n'+
            str(saver['global.armor'][6])+'\n'+
            str(saver['global.weapon'][7])+'\n'+
            str(saver['global.armor'][7])+'\n'+
            str(saver['global.weapon'][8])+'\n'+
            str(saver['global.armor'][8])+'\n'+
            str(saver['global.weapon'][9])+'\n'+
            str(saver['global.armor'][9])+'\n'+
            str(saver['global.weapon'][10])+'\n'+
            str(saver['global.armor'][10])+'\n'+
            str(saver['global.weapon'][11])+'\n'+
            str(saver['global.armor'][11])+'\n'+
            str(saver['global.weapon'][12])+'\n'+
            str(saver['global.armor'][12])+'\n'+
            str(saver['global.weapon'][13])+'\n'+
            str(saver['global.armor'][13])+'\n'+
            str(saver['global.weapon'][14])+'\n'+
            str(saver['global.armor'][14])+'\n'+
            str(saver['global.weapon'][15])+'\n'+
            str(saver['global.armor'][15])+'\n'+
            str(saver['global.weapon'][16])+'\n'+
            str(saver['global.armor'][16])+'\n'+
            str(saver['global.weapon'][17])+'\n'+
            str(saver['global.armor'][17])+'\n'+
            str(saver['global.weapon'][18])+'\n'+
            str(saver['global.armor'][18])+'\n'+
            str(saver['global.weapon'][19])+'\n'+
            str(saver['global.armor'][19])+'\n'+
            str(saver['global.weapon'][20])+'\n'+
            str(saver['global.armor'][20])+'\n'+
            str(saver['global.weapon'][21])+'\n'+
            str(saver['global.armor'][21])+'\n'+
            str(saver['global.weapon'][22])+'\n'+
            str(saver['global.armor'][22])+'\n'+
            str(saver['global.weapon'][23])+'\n'+
            str(saver['global.armor'][23])+'\n'+
            str(saver['global.weapon'][24])+'\n'+
            str(saver['global.armor'][24])+'\n'+
            str(saver['global.weapon'][25])+'\n'+
            str(saver['global.armor'][25])+'\n'+
            str(saver['global.weapon'][26])+'\n'+
            str(saver['global.armor'][26])+'\n'+
            str(saver['global.weapon'][27])+'\n'+
            str(saver['global.armor'][27])+'\n'+
            str(saver['global.weapon'][28])+'\n'+
            str(saver['global.armor'][28])+'\n'+
            str(saver['global.weapon'][29])+'\n'+
            str(saver['global.armor'][29])+'\n'+
            str(saver['global.weapon'][30])+'\n'+
            str(saver['global.armor'][30])+'\n'+
            str(saver['global.weapon'][31])+'\n'+
            str(saver['global.armor'][31])+'\n'+
            str(saver['global.weapon'][32])+'\n'+
            str(saver['global.armor'][32])+'\n'+
            str(saver['global.weapon'][33])+'\n'+
            str(saver['global.armor'][33])+'\n'+
            str(saver['global.weapon'][34])+'\n'+
            str(saver['global.armor'][34])+'\n'+
            str(saver['global.weapon'][35])+'\n'+
            str(saver['global.armor'][35])+'\n'+
            str(saver['global.weapon'][36])+'\n'+
            str(saver['global.armor'][36])+'\n'+
            str(saver['global.weapon'][37])+'\n'+
            str(saver['global.armor'][37])+'\n'+
            str(saver['global.weapon'][38])+'\n'+
            str(saver['global.armor'][38])+'\n'+
            str(saver['global.weapon'][39])+'\n'+
            str(saver['global.armor'][39])+'\n'+
            str(saver['global.weapon'][40])+'\n'+
            str(saver['global.armor'][40])+'\n'+
            str(saver['global.weapon'][41])+'\n'+
            str(saver['global.armor'][41])+'\n'+
            str(saver['global.weapon'][42])+'\n'+
            str(saver['global.armor'][42])+'\n'+
            str(saver['global.weapon'][43])+'\n'+
            str(saver['global.armor'][43])+'\n'+
            str(saver['global.weapon'][44])+'\n'+
            str(saver['global.armor'][44])+'\n'+
            str(saver['global.weapon'][45])+'\n'+
            str(saver['global.armor'][45])+'\n'+
            str(saver['global.weapon'][46])+'\n'+
            str(saver['global.armor'][46])+'\n'+
            str(saver['global.weapon'][47])+'\n'+
            str(saver['global.armor'][47])+'\n'+
            '\n'.join(str(j) for j in saver['global.pocketitem'])+'\n'+
            str(saver['global.tension'])+'\n'+
            str(saver['global.maxtension'])+'\n'+
            str(saver['global.lweapon'])+'\n'+
            str(saver['global.larmor'])+'\n'+
            str(saver['global.lxp'])+'\n'+
            str(saver['global.llv'])+'\n'+
            str(saver['global.lgold'])+'\n'+
            str(saver['global.lhp'])+'\n'+
            str(saver['global.lmaxhp'])+'\n'+
            str(saver['global.lat'])+'\n'+
            str(saver['global.ldf'])+'\n'+
            str(saver['global.lwstrength'])+'\n'+
            str(saver['global.ladef'])+'\n'+
            str(saver['global.litem'][0])+'\n'+
            str(saver['global.phone'][0])+'\n'+
            str(saver['global.litem'][1])+'\n'+
            str(saver['global.phone'][1])+'\n'+
            str(saver['global.litem'][2])+'\n'+
            str(saver['global.phone'][2])+'\n'+
            str(saver['global.litem'][3])+'\n'+
            str(saver['global.phone'][3])+'\n'+
            str(saver['global.litem'][4])+'\n'+
            str(saver['global.phone'][4])+'\n'+
            str(saver['global.litem'][5])+'\n'+
            str(saver['global.phone'][5])+'\n'+
            str(saver['global.litem'][6])+'\n'+
            str(saver['global.phone'][6])+'\n'+
            str(saver['global.litem'][7])+'\n'+
            str(saver['global.phone'][7])+'\n'+
            '\n'.join(str(j) for j in saver['global.flags'])+'\n'+
            str(saver['global.plot'])+'\n'+
            str(saver['global.currentroom'])+'\n'+
            str(saver['global.time'])
        )
    else:           #Chapter 1 save
        newsave=(
            saver['global.truename']+'\n'+
            '\n'.join(saver['global.othername'])+'\n'+
            str(saver['global.char[0]'])+'\n'+
            str(saver['global.char[1]'])+'\n'+
            str(saver['global.char[2]'])+'\n'+
            str(saver['global.gold'])+'\n'+
            str(saver['global.xp'])+'\n'+
            str(saver['global.lv'])+'\n'+
            str(saver['global.inv'])+'\n'+
            str(saver['global.invc'])+'\n'+
            str(saver['global.darkzone'])+'\n'+
            str(saver['global.hp'][0])+'\n'+
            str(saver['global.maxhp'][0])+'\n'+
            str(saver['global.at'][0])+'\n'+
            str(saver['global.df'][0])+'\n'+
            str(saver['global.mag'][0])+'\n'+
            str(saver['global.guts'][0])+'\n'+
            str(saver['global.charweapon'][0])+'\n'+
            str(saver['global.chararmor1'][0])+'\n'+
            str(saver['global.chararmor2'][0])+'\n'+
            str(saver['global.weaponstyle'][0])+'\n'+
            str(saver['global.itemat[0, 0]'])+'\n'+
            str(saver['global.itemdf[0, 0]'])+'\n'+
            str(saver['global.itemmag[0, 0]'])+'\n'+
            str(saver['global.itembolts[0, 0]'])+'\n'+
            str(saver['global.itemgrazeamt[0, 0]'])+'\n'+
            str(saver['global.itemgrazesize[0, 0]'])+'\n'+
            str(saver['global.itemboltspeed[0, 0]'])+'\n'+
            str(saver['global.itemspecial[0, 0]'])+'\n'+
            str(saver['global.itemat[0, 1]'])+'\n'+
            str(saver['global.itemdf[0, 1]'])+'\n'+
            str(saver['global.itemmag[0, 1]'])+'\n'+
            str(saver['global.itembolts[0, 1]'])+'\n'+
            str(saver['global.itemgrazeamt[0, 1]'])+'\n'+
            str(saver['global.itemgrazesize[0, 1]'])+'\n'+
            str(saver['global.itemboltspeed[0, 1]'])+'\n'+
            str(saver['global.itemspecial[0, 1]'])+'\n'+
            str(saver['global.itemat[0, 2]'])+'\n'+
            str(saver['global.itemdf[0, 2]'])+'\n'+
            str(saver['global.itemmag[0, 2]'])+'\n'+
            str(saver['global.itembolts[0, 2]'])+'\n'+
            str(saver['global.itemgrazeamt[0, 2]'])+'\n'+
            str(saver['global.itemgrazesize[0, 2]'])+'\n'+
            str(saver['global.itemboltspeed[0, 2]'])+'\n'+
            str(saver['global.itemspecial[0, 2]'])+'\n'+
            str(saver['global.itemat[0, 3]'])+'\n'+
            str(saver['global.itemdf[0, 3]'])+'\n'+
            str(saver['global.itemmag[0, 3]'])+'\n'+
            str(saver['global.itembolts[0, 3]'])+'\n'+
            str(saver['global.itemgrazeamt[0, 3]'])+'\n'+
            str(saver['global.itemgrazesize[0, 3]'])+'\n'+
            str(saver['global.itemboltspeed[0, 3]'])+'\n'+
            str(saver['global.itemspecial[0, 3]'])+'\n'+
            str(saver['global.spell[0, 0]'])+'\n'+
            str(saver['global.spell[0, 1]'])+'\n'+
            str(saver['global.spell[0, 2]'])+'\n'+
            str(saver['global.spell[0, 3]'])+'\n'+
            str(saver['global.spell[0, 4]'])+'\n'+
            str(saver['global.spell[0, 5]'])+'\n'+
            str(saver['global.spell[0, 6]'])+'\n'+
            str(saver['global.spell[0, 7]'])+'\n'+
            str(saver['global.spell[0, 8]'])+'\n'+
            str(saver['global.spell[0, 9]'])+'\n'+
            str(saver['global.spell[0, 10]'])+'\n'+
            str(saver['global.spell[0, 11]'])+'\n'+
            str(saver['global.hp'][1])+'\n'+
            str(saver['global.maxhp'][1])+'\n'+
            str(saver['global.at'][1])+'\n'+
            str(saver['global.df'][1])+'\n'+
            str(saver['global.mag'][1])+'\n'+
            str(saver['global.guts'][1])+'\n'+
            str(saver['global.charweapon'][1])+'\n'+
            str(saver['global.chararmor1'][1])+'\n'+
            str(saver['global.chararmor2'][1])+'\n'+
            str(saver['global.weaponstyle'][1])+'\n'+
            str(saver['global.itemat[1, 0]'])+'\n'+
            str(saver['global.itemdf[1, 0]'])+'\n'+
            str(saver['global.itemmag[1, 0]'])+'\n'+
            str(saver['global.itembolts[1, 0]'])+'\n'+
            str(saver['global.itemgrazeamt[1, 0]'])+'\n'+
            str(saver['global.itemgrazesize[1, 0]'])+'\n'+
            str(saver['global.itemboltspeed[1, 0]'])+'\n'+
            str(saver['global.itemspecial[1, 0]'])+'\n'+
            str(saver['global.itemat[1, 1]'])+'\n'+
            str(saver['global.itemdf[1, 1]'])+'\n'+
            str(saver['global.itemmag[1, 1]'])+'\n'+
            str(saver['global.itembolts[1, 1]'])+'\n'+
            str(saver['global.itemgrazeamt[1, 1]'])+'\n'+
            str(saver['global.itemgrazesize[1, 1]'])+'\n'+
            str(saver['global.itemboltspeed[1, 1]'])+'\n'+
            str(saver['global.itemspecial[1, 1]'])+'\n'+
            str(saver['global.itemat[1, 2]'])+'\n'+
            str(saver['global.itemdf[1, 2]'])+'\n'+
            str(saver['global.itemmag[1, 2]'])+'\n'+
            str(saver['global.itembolts[1, 2]'])+'\n'+
            str(saver['global.itemgrazeamt[1, 2]'])+'\n'+
            str(saver['global.itemgrazesize[1, 2]'])+'\n'+
            str(saver['global.itemboltspeed[1, 2]'])+'\n'+
            str(saver['global.itemspecial[1, 2]'])+'\n'+
            str(saver['global.itemat[1, 3]'])+'\n'+
            str(saver['global.itemdf[1, 3]'])+'\n'+
            str(saver['global.itemmag[1, 3]'])+'\n'+
            str(saver['global.itembolts[1, 3]'])+'\n'+
            str(saver['global.itemgrazeamt[1, 3]'])+'\n'+
            str(saver['global.itemgrazesize[1, 3]'])+'\n'+
            str(saver['global.itemboltspeed[1, 3]'])+'\n'+
            str(saver['global.itemspecial[1, 3]'])+'\n'+
            str(saver['global.spell[1, 0]'])+'\n'+
            str(saver['global.spell[1, 1]'])+'\n'+
            str(saver['global.spell[1, 2]'])+'\n'+
            str(saver['global.spell[1, 3]'])+'\n'+
            str(saver['global.spell[1, 4]'])+'\n'+
            str(saver['global.spell[1, 5]'])+'\n'+
            str(saver['global.spell[1, 6]'])+'\n'+
            str(saver['global.spell[1, 7]'])+'\n'+
            str(saver['global.spell[1, 8]'])+'\n'+
            str(saver['global.spell[1, 9]'])+'\n'+
            str(saver['global.spell[1, 10]'])+'\n'+
            str(saver['global.spell[1, 11]'])+'\n'+
            str(saver['global.hp'][2])+'\n'+
            str(saver['global.maxhp'][2])+'\n'+
            str(saver['global.at'][2])+'\n'+
            str(saver['global.df'][2])+'\n'+
            str(saver['global.mag'][2])+'\n'+
            str(saver['global.guts'][2])+'\n'+
            str(saver['global.charweapon'][2])+'\n'+
            str(saver['global.chararmor1'][2])+'\n'+
            str(saver['global.chararmor2'][2])+'\n'+
            str(saver['global.weaponstyle'][2])+'\n'+
            str(saver['global.itemat[2, 0]'])+'\n'+
            str(saver['global.itemdf[2, 0]'])+'\n'+
            str(saver['global.itemmag[2, 0]'])+'\n'+
            str(saver['global.itembolts[2, 0]'])+'\n'+
            str(saver['global.itemgrazeamt[2, 0]'])+'\n'+
            str(saver['global.itemgrazesize[2, 0]'])+'\n'+
            str(saver['global.itemboltspeed[2, 0]'])+'\n'+
            str(saver['global.itemspecial[2, 0]'])+'\n'+
            str(saver['global.itemat[2, 1]'])+'\n'+
            str(saver['global.itemdf[2, 1]'])+'\n'+
            str(saver['global.itemmag[2, 1]'])+'\n'+
            str(saver['global.itembolts[2, 1]'])+'\n'+
            str(saver['global.itemgrazeamt[2, 1]'])+'\n'+
            str(saver['global.itemgrazesize[2, 1]'])+'\n'+
            str(saver['global.itemboltspeed[2, 1]'])+'\n'+
            str(saver['global.itemspecial[2, 1]'])+'\n'+
            str(saver['global.itemat[2, 2]'])+'\n'+
            str(saver['global.itemdf[2, 2]'])+'\n'+
            str(saver['global.itemmag[2, 2]'])+'\n'+
            str(saver['global.itembolts[2, 2]'])+'\n'+
            str(saver['global.itemgrazeamt[2, 2]'])+'\n'+
            str(saver['global.itemgrazesize[2, 2]'])+'\n'+
            str(saver['global.itemboltspeed[2, 2]'])+'\n'+
            str(saver['global.itemspecial[2, 2]'])+'\n'+
            str(saver['global.itemat[2, 3]'])+'\n'+
            str(saver['global.itemdf[2, 3]'])+'\n'+
            str(saver['global.itemmag[2, 3]'])+'\n'+
            str(saver['global.itembolts[2, 3]'])+'\n'+
            str(saver['global.itemgrazeamt[2, 3]'])+'\n'+
            str(saver['global.itemgrazesize[2, 3]'])+'\n'+
            str(saver['global.itemboltspeed[2, 3]'])+'\n'+
            str(saver['global.itemspecial[2, 3]'])+'\n'+
            str(saver['global.spell[2, 0]'])+'\n'+
            str(saver['global.spell[2, 1]'])+'\n'+
            str(saver['global.spell[2, 2]'])+'\n'+
            str(saver['global.spell[2, 3]'])+'\n'+
            str(saver['global.spell[2, 4]'])+'\n'+
            str(saver['global.spell[2, 5]'])+'\n'+
            str(saver['global.spell[2, 6]'])+'\n'+
            str(saver['global.spell[2, 7]'])+'\n'+
            str(saver['global.spell[2, 8]'])+'\n'+
            str(saver['global.spell[2, 9]'])+'\n'+
            str(saver['global.spell[2, 10]'])+'\n'+
            str(saver['global.spell[2, 11]'])+'\n'+
            str(saver['global.hp'][3])+'\n'+
            str(saver['global.maxhp'][3])+'\n'+
            str(saver['global.at'][3])+'\n'+
            str(saver['global.df'][3])+'\n'+
            str(saver['global.mag'][3])+'\n'+
            str(saver['global.guts'][3])+'\n'+
            str(saver['global.charweapon'][3])+'\n'+
            str(saver['global.chararmor1'][3])+'\n'+
            str(saver['global.chararmor2'][3])+'\n'+
            str(saver['global.weaponstyle'][3])+'\n'+
            str(saver['global.itemat[3, 0]'])+'\n'+
            str(saver['global.itemdf[3, 0]'])+'\n'+
            str(saver['global.itemmag[3, 0]'])+'\n'+
            str(saver['global.itembolts[3, 0]'])+'\n'+
            str(saver['global.itemgrazeamt[3, 0]'])+'\n'+
            str(saver['global.itemgrazesize[3, 0]'])+'\n'+
            str(saver['global.itemboltspeed[3, 0]'])+'\n'+
            str(saver['global.itemspecial[3, 0]'])+'\n'+
            str(saver['global.itemat[3, 1]'])+'\n'+
            str(saver['global.itemdf[3, 1]'])+'\n'+
            str(saver['global.itemmag[3, 1]'])+'\n'+
            str(saver['global.itembolts[3, 1]'])+'\n'+
            str(saver['global.itemgrazeamt[3, 1]'])+'\n'+
            str(saver['global.itemgrazesize[3, 1]'])+'\n'+
            str(saver['global.itemboltspeed[3, 1]'])+'\n'+
            str(saver['global.itemspecial[3, 1]'])+'\n'+
            str(saver['global.itemat[3, 2]'])+'\n'+
            str(saver['global.itemdf[3, 2]'])+'\n'+
            str(saver['global.itemmag[3, 2]'])+'\n'+
            str(saver['global.itembolts[3, 2]'])+'\n'+
            str(saver['global.itemgrazeamt[3, 2]'])+'\n'+
            str(saver['global.itemgrazesize[3, 2]'])+'\n'+
            str(saver['global.itemboltspeed[3, 2]'])+'\n'+
            str(saver['global.itemspecial[3, 2]'])+'\n'+
            str(saver['global.itemat[3, 3]'])+'\n'+
            str(saver['global.itemdf[3, 3]'])+'\n'+
            str(saver['global.itemmag[3, 3]'])+'\n'+
            str(saver['global.itembolts[3, 3]'])+'\n'+
            str(saver['global.itemgrazeamt[3, 3]'])+'\n'+
            str(saver['global.itemgrazesize[3, 3]'])+'\n'+
            str(saver['global.itemboltspeed[3, 3]'])+'\n'+
            str(saver['global.itemspecial[3, 3]'])+'\n'+
            str(saver['global.spell[3, 0]'])+'\n'+
            str(saver['global.spell[3, 1]'])+'\n'+
            str(saver['global.spell[3, 2]'])+'\n'+
            str(saver['global.spell[3, 3]'])+'\n'+
            str(saver['global.spell[3, 4]'])+'\n'+
            str(saver['global.spell[3, 5]'])+'\n'+
            str(saver['global.spell[3, 6]'])+'\n'+
            str(saver['global.spell[3, 7]'])+'\n'+
            str(saver['global.spell[3, 8]'])+'\n'+
            str(saver['global.spell[3, 9]'])+'\n'+
            str(saver['global.spell[3, 10]'])+'\n'+
            str(saver['global.spell[3, 11]'])+'\n'+
            str(saver['global.boltspeed'])+'\n'+
            str(saver['global.grazeamt'])+'\n'+
            str(saver['global.grazesize'])+'\n'+
            str(saver['global.item'][0])+'\n'+
            str(saver['global.keyitem'][0])+'\n'+
            str(saver['global.weapon'][0])+'\n'+
            str(saver['global.armor'][0])+'\n'+
            str(saver['global.item'][1])+'\n'+
            str(saver['global.keyitem'][1])+'\n'+
            str(saver['global.weapon'][1])+'\n'+
            str(saver['global.armor'][1])+'\n'+
            str(saver['global.item'][2])+'\n'+
            str(saver['global.keyitem'][2])+'\n'+
            str(saver['global.weapon'][2])+'\n'+
            str(saver['global.armor'][2])+'\n'+
            str(saver['global.item'][3])+'\n'+
            str(saver['global.keyitem'][3])+'\n'+
            str(saver['global.weapon'][3])+'\n'+
            str(saver['global.armor'][3])+'\n'+
            str(saver['global.item'][4])+'\n'+
            str(saver['global.keyitem'][4])+'\n'+
            str(saver['global.weapon'][4])+'\n'+
            str(saver['global.armor'][4])+'\n'+
            str(saver['global.item'][5])+'\n'+
            str(saver['global.keyitem'][5])+'\n'+
            str(saver['global.weapon'][5])+'\n'+
            str(saver['global.armor'][5])+'\n'+
            str(saver['global.item'][6])+'\n'+
            str(saver['global.keyitem'][6])+'\n'+
            str(saver['global.weapon'][6])+'\n'+
            str(saver['global.armor'][6])+'\n'+
            str(saver['global.item'][7])+'\n'+
            str(saver['global.keyitem'][7])+'\n'+
            str(saver['global.weapon'][7])+'\n'+
            str(saver['global.armor'][7])+'\n'+
            str(saver['global.item'][8])+'\n'+
            str(saver['global.keyitem'][8])+'\n'+
            str(saver['global.weapon'][8])+'\n'+
            str(saver['global.armor'][8])+'\n'+
            str(saver['global.item'][9])+'\n'+
            str(saver['global.keyitem'][9])+'\n'+
            str(saver['global.weapon'][9])+'\n'+
            str(saver['global.armor'][9])+'\n'+
            str(saver['global.item'][10])+'\n'+
            str(saver['global.keyitem'][10])+'\n'+
            str(saver['global.weapon'][10])+'\n'+
            str(saver['global.armor'][10])+'\n'+
            str(saver['global.item'][11])+'\n'+
            str(saver['global.keyitem'][11])+'\n'+
            str(saver['global.weapon'][11])+'\n'+
            str(saver['global.armor'][11])+'\n'+
            str(saver['global.item'][12])+'\n'+
            str(saver['global.keyitem'][12])+'\n'+
            str(saver['global.weapon'][12])+'\n'+
            str(saver['global.armor'][12])+'\n'+
            str(saver['global.tension'])+'\n'+
            str(saver['global.maxtension'])+'\n'+
            str(saver['global.lweapon'])+'\n'+
            str(saver['global.larmor'])+'\n'+
            str(saver['global.lxp'])+'\n'+
            str(saver['global.llv'])+'\n'+
            str(saver['global.lgold'])+'\n'+
            str(saver['global.lhp'])+'\n'+
            str(saver['global.lmaxhp'])+'\n'+
            str(saver['global.lat'])+'\n'+
            str(saver['global.ldf'])+'\n'+
            str(saver['global.lwstrength'])+'\n'+
            str(saver['global.ladef'])+'\n'+
            str(saver['global.litem'][0])+'\n'+
            str(saver['global.phone'][0])+'\n'+
            str(saver['global.litem'][1])+'\n'+
            str(saver['global.phone'][1])+'\n'+
            str(saver['global.litem'][2])+'\n'+
            str(saver['global.phone'][2])+'\n'+
            str(saver['global.litem'][3])+'\n'+
            str(saver['global.phone'][3])+'\n'+
            str(saver['global.litem'][4])+'\n'+
            str(saver['global.phone'][4])+'\n'+
            str(saver['global.litem'][5])+'\n'+
            str(saver['global.phone'][5])+'\n'+
            str(saver['global.litem'][6])+'\n'+
            str(saver['global.phone'][6])+'\n'+
            str(saver['global.litem'][7])+'\n'+
            str(saver['global.phone'][7])+'\n'+
            '\n'.join(str(j) for j in saver['global.flags'])+'\n'+
            str(saver['global.plot'])+'\n'+
            str(saver['global.currentroom'])+'\n'+
            str(saver['global.time'])+'\n'
        )
    with open(filename,'w') as g:g.write(newsave)

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
                returns.append(0) #Tenna editor doesn't like my Normal
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



if __name__ == "__main__":
    print("You're running the wrong script!!")