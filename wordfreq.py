#!/bin/python
import glob

d = {}
liuDict={}
for f in glob.glob("assets/*.txt"):
    print "processing " + f + " ..."
    fi = open(f, 'r')
    s = fi.read()
    fi.close()
    for c in s.decode('utf8'):
        if not d.has_key(c):
            d[c]=1
        else:
            d[c]=d[c]+1
    pass
    
print "reading liu.txt ..."

f=open("liu.txt",'r')
for l in f:
    x=l.split()
    res=x[0].decode('utf8') # result
    sol=x[1:]               # solution
    for s in sol:
        if liuDict.has_key(s):
            liuDict[s]=liuDict[s]+[res]
        else:
            liuDict[s]=[res]

f.close()
f=open("output.txt",'w+')
f.write("BEGIN_TABLE\n")
for i in liuDict:
    for c in liuDict[i]:
        if d.has_key(c):
            s=("%s\t%s\t%d\n" % (i.lower(),c,d[c]+100))
        else:
            s=("%s\t%s\t%d\n" % (i.lower(),c,100))
        
        f.write(s.encode('utf8'))
        pass

f.write("END_TABLE\n\n")
f.close()

print "done"