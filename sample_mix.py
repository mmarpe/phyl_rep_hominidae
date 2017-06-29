#!/usr/bin/python

from itertools import combinations, product
import sys
from subprocess import call

print "Uso: sample_mix.py InputFile"

try:
	file = sys.argv[1]
except:
	file = raw_input("Introduce normalized cluster abundances file: ")

f = open(file).readlines()
hd = f[0] 
hd =hd.split()

print "===Dictionary==="
didi={}

for e in hd:
	data = e.split("_")
	if data[0] in didi:
		didi[data[0]].append(e)
	else:
		didi[data[0]]=[e]

#print didi

print "===Combinations==="

lili=[]

for i in didi:
	if len(didi[i])>= 2:
		lili.append(list(combinations(didi[i],2)))
	else:	
		q=list(didi[i])
		lili.append([q])

#print lili

x=list(product(*lili))
#print x

print "===Final file of combinations==="
sl=[]
for y in x:
	l=[]
	for u in y:
		if len(u)>= 2:
			for t in u:
				z=l.append(t)
		else:
			s=l.append(u[0])
	sl.append(l)

#print sl #Este fichero es el de las combinacions

db=[]

for n in range(0, len(hd)):
	db.append([])

for line in f:
	info=line.split()
	for n in range(0, len(info)):
		db[n].append(info[n])

#print db
		
dict_db={}

for i in db:
	dict_db[i[0]]=i[1:]

#print dict_db

print "===Starting phylogenetics analysis==="

c=open("pipeline.run","w")
c.write("procedure tmp ;\nhold 10000 ;\ntaxname= ;\noutgroup MMUL_1 ;\nienum ;\nnelsen * ;\ntsave * tmp.tree ;\nsave ;\nttag= ;\nresample sym replications 10000 ;\nsave *;\nexport - tmp.nex;\nquit\n")

c.close()

call("chmod +x pipeline.run", shell=True)

for l in sl:
	w=open("tmp", "w")
	w.write("nstates cont ;\nxread\n1000 11\n")
	for ind in l:
		w.write(ind + " " + " ".join(dict_db[ind])+"\n")
	
	w.write(";\ncc-.;\nproc/;")
	w.close()
	
	print "TNT"
	call ("./tnt procedure pipeline.run", shell=True)
	call ("rm tmp.tree", shell=True)
	call ("mv tmp.nex %s" % ( "".join(l)+".nex"), shell=True)
	print "===Tree to PDF==="
	call("figtree -graphic PDF %s %s " % ("".join(l)+".nex",  "".join(l) + ".pdf"), shell=True )

print "Done!! :-)"














