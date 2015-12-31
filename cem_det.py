 ## Getting the file
count_harry=0
count_hermione=0  
count_snape=0
count_ron=0
count_dumbledore=0  
count_hermione_harry=0
count_dumbledore_harry=0
count_ron_harry=0
count_snape_harry=0
count_dumbledore_ron=0
count_harry_ron=0
count_hermione_ron=0
count_snape_ron=0
count_dumbledore_hermione=0
count_harry_hermione=0
count_ron_hermione=0
count_snape_hermione=0
count_harry_dumbledore=0
count_ron_dumbledore=0
count_snape_dumbledore=0
count_hermione_dumbledore=0
count_harry_snape=0
count_ron_snape=0
count_dumbledore_snape=0
count_hermione_snape=0
Harry=dict()
Hermione=dict()
Snape=dict()
Ron=dict()
Hagrid=dict()
stack=("Harry","Hermione","Snape","Ron","Hagrid")
fname="text.txt"
fh=open(fname)
## File got 
## Now conversion to string 
for line in fh:
    line=line.rstrip()
    word=line.split()
    if ("Harry" in word or "harry" in word):
        count_harry+=1
        if "Hermione" in word or "hermione" in word:
            count_hermione_harry+=1
        if  "Ron" in word or "ron" in word:
            count_ron_harry+=1
        if "Dumbledore" in word or "dumbledore" in word:
            count_dumbledore_harry+=1
        if "Snape" in word or "snape" in word:
            count_snape_harry+=1       
    if "Ron" in word or "ron" in word:
        count_ron+=1
        if "Hermione" in word or "hermione" in word:
            count_hermione_ron+=1
        if  "Harry" in word or "harry" in word:
            count_harry_ron+=1
        if "Dumbledore" in word or "dumbledore" in word:
            count_dumbledore_ron+=1
        if "Snape" in word or "snape" in word:
            count_snape_ron+=1
    if "Hermione" in word or "hermione" in word:
        count_hermione+=1
        if "Ron" in word or "ron" in word:
            count_ron_hermione+=1
        if  "Harry" in word or "harry" in word:
            count_harry_hermione+=1
        if "Dumbledore" in word or "dumbledore" in word:
            count_dumbledore_hermione+=1
        if "Snape" in word or "snape" in word:
            count_snape_hermione+=1
    if "Dumbledore" in word or "dumbledore" in word:
        count_dumbledore+=1
        if "Ron" in word or "ron" in word:
            count_ron_dumbledore+=1
        if  "Harry" in word or "harry" in word:
            count_harry_dumbledore+=1
        if "Hermione" in word or "hermione" in word:
            count_hermione_dumbledore+=1
        if "Snape" in word or "snape" in word:
            count_snape_dumbledore+=1
    if "Snape" in word or "snape" in word:
        count_snape+=1
        if "Ron" in word or "ron" in word:
            count_ron_snape+=1
        if  "Harry" in word or "harry" in word:
            count_harry_snape+=1
        if "Hermione" in word or "hermione" in word:
            count_hermione_snape+=1
        if "Snape" in word or "snape" in word:
            count_dumbledore_snape+=1
print "Harry",count_harry
print "Hermione",count_hermione
print "Ron",count_ron
print "Dumbledore",count_dumbledore
print "Snape",count_snape
print "correlation of hermione to harry ::",float(count_hermione_harry)/count_harry
print "correlation of ron to harry ::",float(count_ron_harry)/count_harry
print "correlation of snape to harry ::",float(count_snape_harry)/count_harry
print "correlation of dumbledore to harry ::",float(count_dumbledore_harry)/count_harry
print "*"*100
print "correlation of hermione to ron ::",float(count_hermione_ron)/count_ron
print "correlation of harry to ron ::",float(count_harry_ron)/count_ron
print "correlation of snape to ron ::",float(count_snape_ron)/count_ron
print "correlation of dumbledore to ron ::",float(count_dumbledore_ron)/count_ron
print "*"*100
print "correlation of ron to hermione ::",float(count_ron_hermione)/count_hermione
print "correlation of harry to hermione ::",float(count_harry_hermione)/count_hermione
print "correlation of snape to hermione ::",float(count_snape_hermione)/count_hermione
print "correlation of dumbledore to hermione ::",float(count_dumbledore_hermione)/count_hermione
print "*"*100
print "correlation of ron to dumbledore ::",float(count_ron_dumbledore)/count_dumbledore
print "correlation of harry to dumbledore ::",float(count_harry_dumbledore)/count_dumbledore
print "correlation of snape to dumbledore ::",float(count_snape_dumbledore)/count_dumbledore
print "correlation of hermione to dumbledore ::",float(count_hermione_dumbledore)/count_dumbledore
print "*"*100
print "correlation of ron to snape ::",float(count_ron_snape)/count_snape
print "correlation of harry to snape ::",float(count_harry_snape)/count_snape
print "correlation of dumbledore to snape  ::",float(count_dumbledore_snape)/count_snape
print "correlation of hermione to snape ::",float(count_hermione_snape)/count_snape
## correlation gardient
print "*"*400
print "*"*400
print "cr of ron and hermione is ::",100*((count_hermione_ron*count_ron_hermione)/float(count_hermione*count_ron))
print "cr of ron and harry is ::",100*((count_harry_ron*count_ron_harry)/float(count_harry*count_ron))
print "cr of ron and snape is ::",100*((count_snape_ron*count_ron_snape)/float(count_snape*count_ron))
print "*"*100
print "cr of harry and hermione is ::",100*((count_hermione_harry*count_harry_hermione)/float(count_hermione*count_harry))
print "cr of harry and snape is ::",100*((count_snape_harry*count_harry_snape)/float(count_snape*count_harry))
print "cr of harry and dumbledore is ::",100*((count_dumbledore_harry*count_harry_dumbledore)/float(count_dumbledore*count_harry))
print "*"*100
print "cr of hermione and dumbledore is ::",100*((count_dumbledore_hermione*count_hermione_dumbledore)/float(count_dumbledore*count_hermione))
print "cr of hermione and snape is ::",100*((count_snape_hermione*count_hermione_snape)/float(count_snape*count_hermione))
print "*"*100
print "cr of snape and dumbledore is ::",100*((count_snape_dumbledore*count_dumbledore_snape)/float(count_snape*count_dumbledore))
