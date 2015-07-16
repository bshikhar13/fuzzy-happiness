X = []				#The Input Vector
Y = []				# The output value


import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="bshikhar13",
                     db="nn_cdr")



query_genuine = "SELECT * FROM cdr_voice_genuine WHERE 1"
query_fraud = "SELECT * FROM cdr_voice_fraud WHERE 1"

cur_genuine = db.cursor()
cur_fraud = db.cursor()

cur_genuine.execute(query_genuine)
cur_fraud.execute(query_fraud)

count = 0
mytemp = 0
myimsi = "0"
myimei = "0"

for row_genuine in cur_genuine.fetchall():
	
	starttime = int(row_genuine[2])
	endtime = int(row_genuine[3])
	
	imsi = row_genuine[1]
	imei = row_genuine[0]
	
	y = int(row_genuine[4])

	idletime = 0
	if myimsi is myimsi and myimei is myimei:
		
		idletime = starttime - mytemp
		mytemp = endtime
		
	else:
		idletime = 0
		myimei = imei
		myimsi = imsi
		mytemp = endtime




	Xtuple = []
	Xtuple.append(starttime)
	Xtuple.append(endtime)
	Xtuple.append(idletime)
	Xtuple.append(y)
	X.append(Xtuple)
	count = count + 1

print X[0]
print X[1]
print X[2]



count = 0
mytemp = 0
myimsi = "0"
myimei = "0"


for row_fraud in cur_fraud.fetchall():
	
	starttime = int(row_fraud[2])
	endtime = int(row_fraud[3])
	
	imsi = row_fraud[1]
	imei = row_fraud[0]
	
	y = int(row_fraud[4])

	idletime = 0
	if myimsi is myimsi and myimei is myimei:
		
		idletime = starttime - mytemp
		mytemp = endtime
		
	else:
		idletime = 0
		myimei = imei
		myimsi = imsi
		mytemp = endtime

	Xtuple = []
	Xtuple.append(starttime)
	Xtuple.append(endtime)
	Xtuple.append(idletime)
	Xtuple.append(y)
	X.append(Xtuple)


print X[249607]
print X[249608]
print len(X)