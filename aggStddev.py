import sys 
from collections import defaultdict
y=defaultdict(float) 
yc=defaultdict(int)
for line in sys.stdin:
	lines=line.split('\t')
	val=float(lines[0])
	val=int(val)
	y[val]+=float(lines[1])
	yc[val]+=1


for item in sorted(y.keys()):

	print "{}\t{}".format(item, y[item]/yc[item])


