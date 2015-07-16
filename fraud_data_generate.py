def fraud_data_generate():
	import random	

	number_of_unique_IMSI = 100
	IMSI_list = []
	initialIMSI = 700025421542369
	temp = initialIMSI
	for i in range(0,number_of_unique_IMSI):
		temp = temp + random.randint(1000,10000)
		IMSI_list.append(temp)

	#print IMSI_list
	#print len(list(set(IMSI_list)))
	

	number_of_unique_IMEI = 100
	IMEI_list = []
	initialIMEI = 800025421542369
	temp = initialIMEI
	for i in range(0,number_of_unique_IMEI):
		temp = temp + random.randint(1000,10000)
		IMEI_list.append(temp)

	#print IMEI_list
	#print len(list(set(IMEI_list)))

	imei_imsi_pair = zip(IMSI_list,IMEI_list)
	cdr = []
	
	activity = []

	for i in range(0,len(imei_imsi_pair)):
		temp = random.randint(5,500)
		activity.append(temp)
	
	#print imei_imsi_pair
	for i in range(0,len(imei_imsi_pair)) :
		
		starttime = random.randint(10,100)
		temp = []

		for j in range (0,activity[i]):
			
			imsi = imei_imsi_pair[i][0]
			imei = imei_imsi_pair[i][1]
			
			starttimeforcdr = starttime
			duration = random.randint(10,300)									#For Fake SIms this duration will be less so the limit will be low
			endtimeforcdr = starttimeforcdr + duration
			starttime = endtimeforcdr + random.randint(50,250)				#For Fake sims this limit will be very less as the idle duration between two calls

			cdrtuple = []

			cdrtuple.append(imei)
			cdrtuple.append(imsi)
			
			cdrtuple.append(starttimeforcdr)
			cdrtuple.append(endtimeforcdr)
			cdrtuple.append('0')
			cdr.append(cdrtuple)


	return cdr	


#break_the_number(1000000,10000)
