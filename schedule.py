import pandas as pd
schedule_day = pd.date_range('20180101','20221231',freq='W-SAT')
weeks=0

for i in schedule_day:
	year = i.strftime('%Y')
	month = i.strftime('%m')
	day = i.strftime('%d')
	date = i.strftime('%Y%m%d')
	if (int(month) == 12) and (int(day) >= 25):
		print("---------------------")
		continue 

	issue = 9073+weeks
	print(issue, date)
	print("http://audiocdn.economist.com/sites/default/files/AudioArchive/{0}/{2}/Issue_{1}_{2}_The_Economist_Full_edition.zip".format(year, issue, date))
	weeks=weeks+1
