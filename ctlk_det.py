import collections 
import numpy as np
import matplotlib.pyplot as plt
graph=list()
fig = plt.figure()
ax = fig.add_subplot(111)
## Getting the file
count=dict()
count2=list()
total=0
i=0
dat=dict()
fname="text_mod_alp.txt"
fh=open(fname)
## File got 
## Now conversion to string 
for line in fh:
	line=line.rstrip()
	word=line.split()
	for item in word:
		if item not in count:
			count[item]=1
		else :
			count[item]=count[item]+1
for key in count:
	total+=count[key]
print "Total number of words are ",total
print "Total number of unique words are ",len(count)
index_of_sim=len(count)/float(total)
## make this smaller when done
print "So index of similarity is ",index_of_sim
print "Harry ::",count["harry"]
print "Ron ::",count["ron"]
print "Hermione ::",count["hermione"]
print "Hagrid ::",count["hagrid"]
print "Snape ::",count["snape"]
print "Dumbledore ::",count["dumbledore"]
print "Voldemort ::",count["voldemort"]
graph.append(count["harry"])
graph.append(count["ron"])
graph.append(count["hermione"])
graph.append(count["hagrid"])
graph.append(count["snape"])
ind=np.arange(len(graph))
width=0.35
## graph list now carries all the essentials
## still to figure out how to arrange different ax
rects=ax.bar(ind,graph,width,
             color='blue' )

plt.show()
