 ## Getting the file
ly=0
ing=0
dash=0
q=0
ed=0
fname="text_mod_alp.txt"
fh=open(fname)
fh1=open("mf_alp.txt",'w')
## File got 
## Now conversion to string 
for line in fh:
	line=line.rstrip()
	word=line.split()
	for item in word:
		if item[len(item)-2::] == "ly":
			ly +=1
		if item[len(item)-3::] == "ing":
			ing +=1
		if "!" in item:
			dash +=1
		if "?" in item:
			q+=1
		if item[len(item)-2::] == "ed":
			ed+=1
print "words with 'ly' ::",ly
print "words with 'ing' ::",ing
print "use of '!' ::",dash
print "use of '?'::",q
print "words with 'ed' ::",ed