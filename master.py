# 0   is fraud and 1 is genuine

from genuine_data_generate import *
from fraud_data_generate import *
genuine_data = genuine_data_generate()
fraud_data = fraud_data_generate()

import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="bshikhar13",
                     db="nn_cdr")

cur = db.cursor()

for i in range(0,len(genuine_data)-1):
	#print "YO"

	cur.execute("INSERT INTO cdr_voice_genuine VALUES (%s,%s,%s,%s,%s)",(genuine_data[i][0],genuine_data[i][1],genuine_data[i][2],genuine_data[i][3],genuine_data[i][4]))
	#db.commit()

for i in range(0,len(fraud_data)-1):
	#print "YO"
	cur.execute("INSERT INTO cdr_voice_fraud VALUES (%s,%s,%s,%s,%s)",(fraud_data[i][0],fraud_data[i][1],fraud_data[i][2],fraud_data[i][3],fraud_data[i][4]))
	
	#db.commit()

db.close()