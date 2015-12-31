import collections 
## Getting the file
count=dict()
total=0
i=0
dat=dict()
fname="text_mod_det.txt"
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
#for key in  sorted(count.values()):
#	print "%s : %s" (key,count[key])
#for key, value in sorted(count.iteritems(), key=lambda (k,v): (v,k)):
#    print "%s: %s" % (key, float(value)/total)
print "The number of time 'Harry' has been used :: ",count["harry"]
print "The number of time 'Hagrid' has been used :: ",count["hagrid"]
print "The number of time 'Hermione' has been used :: ",count["hermione"]
print "The number of time 'Ron' has been used :: ",count["ron"]
print "The number of time 'Malfoy' has been used :: ",count["malfoy"]
print "The number of time 'Snape' has been used :: ",count["snape"]
#for key in  sorted(count.values()):
#	print "%s : %s" (key,count[key])
#for key, value in sorted(count.iteritems(), key=lambda (k,v): (v,k)):
#    print "%s: %s" % (key, float(value)/total)
dat=sorted(count.iteritems(), key=lambda (k,v): (v,k))
print dat[len(dat)-100::]