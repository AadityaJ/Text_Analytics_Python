## pre coding done
## Getting the file
fname="text.txt"
fh=open(fname)
fh2=open("text_mod_det.txt",'w')  ## change to "text_mod_det.txt" when in need
fh2.seek(0,0)
## File got 
## Now conversion to string 
for line in fh:
	line=line.rstrip()
	word=line.split()
	##module 1 done
	for item in word:
		item=item.lower()
		if item and item[0].isalpha() and item[len(item)-1].isalpha() :  ## word without any problem
			print item
			item=item+' '
			fh2.write(item)
		else :
			if not item[0].isalpha():  ## begins with punctuation
				print item[1::]
				item=item+' '
				fh2.write(item[1::])
			else :  					## ends with punctuation
				print item[:len(item)-1:]
				item=item[:len(item)-1:]
				item=item+' '
				fh2.write(item)
fh.close()
fh2.close()