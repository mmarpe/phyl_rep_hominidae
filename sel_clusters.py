#!/usr/bin/python

from itertools import combinations, product
import sys
from subprocess import call

print "Uso: sel_clusters.py InputMinReads InputSum"

try:
	reads = sys.argv[1]
	reads=str(reads)
except:
	reads = raw_input("Minimum number of reads per species: ")

try:
	sum = sys.argv[2]
except:
	sum = raw_input ("Introduce sum abundances file: ")

s=open(sum).readlines()
db=[]

for line in s:
	info=line.split()
	#for n in range(0, len(info)):
	db.append(info)


#print db
w=open("discarded_clusters","w")
r=open("clean_output", "w")
for c in db:
	if c[1] <= reads :
		if c[5] <= reads :
			if c[2] >= reads:
				if c[3] >= reads:
					if c[4] >= reads:
						w.write(" ".join(c)+"\n")
					else:
						r.write(" ".join(c)+"\n")
				else:
					r.write(" ".join(c)+"\n")
			else: 
				r.write(" ".join(c)+"\n")
		else:
			r.write(" ".join(c)+"\n")

	else:
		r.write(" ".join(c)+"\n")	
					
w.close()
r.close()




#call("sed -i -e 's/^/cl/g' %s "%(sum), shell=True)
#call("sed -i -e 's/$/\n/g' %s "%(sum), shell=True)
#call("sed -i -e 's/^/cl/g' %s "%(file), shell=True)
#call("sed -i -e 's/$/\n/g' %s "% (file),shell=True)
#call("grep -v 0,000 %s > tmp"%(sum),shell=True)
#call("awk {'print $1'} tmp > tmp_c ",shell=True)
#call("sed -i -e 's/\t/_/g' %s" %(file),shell=True)
#call("fgrep -f tmp_c %s > %s"% (file, file+"_sel.txt"),shell=True)












