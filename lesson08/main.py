import dbase
import files

l = dbase.newtable()
dbase.addrecord(l)
dbase.addrecord(l)
#print(l)
#dbase.printtable(l)
files.savetojson(l)