import pulp 
from collections import defaultdict
import sys


def read_file(filepath):
	y=defaultdict(float)

	f=file(filepath)

	for line in f:
		lines=line.split('\t')
		if float(lines[1])>3.5:
			y[int(lines[0])]=float(lines[1])

	return y 


def getTarget(distFilePath,k):

	y=defaultdict(float)
	f=file(distFilePath)

	for line in f:
		lines=line.split('\t')
		y[int(lines[0])]=k/float(lines[1])/4

	return y 

def operation(y,zd):
	dy=defaultdict(int)

	for item in y.keys():
		if item not in zd:
			zd[item]=zd[item+1]
			
		if y[item]>zd[item]+5:
			dy[item]=-1
		else:
			dy[item]=1
	return dy 


# def 
# def sumCandiate(y,)


y=read_file(sys.argv[1])
max_degree=max(y.keys())
# print max_degree

nv=sum(y.values()) 
k=int(sys.argv[3])
zd=getTarget(sys.argv[2],k)
# print zd 
xd=operation(y,zd)

pvals=[item for item in range(max_degree+1)]
# print pvals

x=pulp.LpVariable.dicts('change', pvals,lowBound = 0) 
sch_model=pulp.LpProblem('scheduing problem', pulp.LpMinimize)



sch_model+=sum([x[val] for val in pvals])

sch_model+=sum([x[val]*xd[val] for val in pvals])<=0,"maximum_number_of_nodes"

for val in pvals:
	sch_model+=y[val]+xd[val]*x[val]>=zd[val], "the minimal count{}".format(val)
	if xd[val]<0:
		# print val 
		sch_model+=0.25*y[val]>=x[val], "the change constraint{}".format(val)

# print sch_model

sch_model.solve()




for val in pvals:
	# print "{}\t{}".format(val,x[val].value()*xd[val])
	print "{}\t{}".format(val,x[val].value()*xd[val]+y[val])

