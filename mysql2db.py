import MySQLdb as mdb
import sys

try:
    fin = open("D:\\1.jpg","rb")
    img = fin.read()
    fin.close()

except IOError, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
try:
    conn = mdb.connect(host='localhost',user='root',
       passwd='admin@123', db='dwp')

except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[0])
    print e
    sys.exit(1)
try:
    cursor = conn.cursor()
    cursor.execute("INSERT` INTO Images SET Data='%s'" % \
        mdb.escape_string(img))
    conn.commit()
    cursor.close()
    conn.close()

except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

