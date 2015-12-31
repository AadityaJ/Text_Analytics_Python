 ## Getting the file
count =0
fname="text_mod_det.txt"
fh=open(fname)
## File got 
## Now conversion to string 
for line in fh:
	line=line.rstrip()
	word=line.split()
	#print word[1][1]
	for i in range(len(word)-1):
		if word[i][0] == word[i+1][0]:
			#print word[i],word[i+1]
			count+=1
print "Total number of words which start with similar sounds are ::",count 
