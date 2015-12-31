import collections 
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
index_of_sim=(len(count)/float(total))
print "So index of similarity is ",index_of_sim
