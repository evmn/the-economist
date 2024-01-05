import pandas as pd
# 8663  2010
# 8714  2011
# 8766  2012
# 8817  2013
# 8868  2014
# 8919  2015
# 8970  2016
# 9022  2017
# 9073  2018
# 9124  2019
# 9175  2020
# 9226  2021
#       http://audiocdn.economist.com/sites/default/files/AudioArchive/2012/20120804/Issue_8796_20120804_The_Economist_Full_edition.zip
#       Issue_8796_20120804 is the first audio version I can download 2021-11-06

schedule_day = pd.date_range('20120101','20241231',freq='W-SAT')
weeks=0

for i in schedule_day:
	year = i.strftime('%Y')
	month = i.strftime('%m')
	day = i.strftime('%d')
	date = i.strftime('%Y%m%d')
	issue = 8766+weeks
	if ((int(month) != 12) or (int(day) < 25)) and not ((int(year) >= 2022) and (int(month) == 8) and (int(day) <= 7)):
#	if (int(month) == 12) and (int(day) >= 24):
#		weeks=weeks+0
#	else:
#		print(issue, date)
#               print("./scrap.sh {0}-{1}-{2} {3}".format(year, month, day, issue))
		print("http://audiocdn.economist.com/sites/default/files/AudioArchive/{0}/{2}/Issue_{1}_{2}_The_Economist_Full_edition.zip".format(year, issue, date))
		#print("{2}|[{1}](http://audiocdn.economist.com/sites/default/files/AudioArchive/{0}/{2}/Issue_{1}_{2}_The_Economist_Full_edition.zip)".format(year, issue, date))
		weeks=weeks+1
