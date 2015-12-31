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
#for key in  sorted(count.values()):
#	print "%s : %s" (key,count[key])
#for key, value in sorted(count.iteritems(), key=lambda (k,v): (v,k)):
#    print "%s: %s" % (key, float(value)/total)
dat=sorted(count.iteritems(), key=lambda (k,v): (v,k))
#print dat[len(dat)-100::]
for i in range(0,100):
	k=str(dat[len(dat)-1-i::])
	k=k.replace('(','')
	k=k.replace('[','')
	k=k.replace(']','')
	k=k.replace(')','')
	print k,'\n'
