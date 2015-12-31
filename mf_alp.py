import collections
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
graph=list()
 ## Getting the file
count=dict()
count2=dict()
fname="text_mod_alp.txt"
fh=open(fname)
fh1=open("mf_alp.txt",'w')
## File got 
## Now conversion to string
alphb=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z') 
for line in fh:
	line=line.rstrip()
	word=line.split()
	for item in word:
		for key in alphb:
			if item.startswith(key):
				if key not in count:
					count[key]=1
				else:
					count[key]+=1
for key in sorted(count.iterkeys()):
    count2[key]=count[key]
for item in alphb:
    if not item == 'x':
        graph.append(count2[item])
ind=np.arange(len(graph))
width=0.35
print len(alphb)
print len(graph)
print graph
print alphb
plt.plot(graph)
plt.show() 
            