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
	query = "INSERT INTO cdr_voice_genuine VALUES (" + str(genuine_data[i][0]) + " ," + str(genuine_data[i][1]) + " ," + str(genuine_data[i][2]) + " ," + str(genuine_data[i][3]) + " )"
	cur.execute(query)
	db.commit()

for i in range(0,len(fraud_data)-1):
	#print "YO"
	query = "INSERT INTO cdr_voice_fraud VALUES (" + str(fraud_data[i][0]) + " ," + str(fraud_data[i][1]) + " ," + str(fraud_data[i][2]) + " ," + str(fraud_data[i][3]) + " )"
	cur.execute(query)
	db.commit()

db.close()