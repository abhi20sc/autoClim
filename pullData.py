import wget
import os

def downloadData():
	monthConversion = {
		"January" : [1,31],
		"February" : [2,28],
		"March" : [3,31],
		"April" : [4,30],
		"May" : [5,31],
		"June" : [6,30],
		"July" : [7,31],
		"August" : [8,31],
		"September" : [9,30],
		"October" : [10,31],
		"November" : [11,30],
		"December" : [12,31]
	}
 	## Validation and input
	yearAccep, monthAccep, dayAccep = False, False, False
	inAccep = False
	while inAccep == False:
		year = int(input("Year?"))
		month = input("Month?")
		date = int(input("Date?"))
		if year > 0 and year < 2022:
			yearAccep = True
		if monthConversion.get(month) is not None:
			monthAccep = True
			monthNum = (monthConversion[month])[0]
			if date > 0 and date < (monthConversion[month])[1]:
				dateAccep = True
		if dateAccep == True and monthAccep == True and yearAccep == True:
			inAccep = True
	# Clearing all older files from directory.
	outPath = 'datasets/'
	filelist = [ f for f in os.listdir(outPath)]
	for file in filelist:
		os.remove(os.path.join(outPath, file))
	# Downloading data.
	airTemp_surface = "ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface/air.sig995." + str(year) + ".nc"
	airTemp_midLevels = "ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/air." + str(year) + ".nc"
	zonal_surface = 'ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface/uwnd.sig995.' + str(year) + '.nc'
	zonal_midLevels = 'ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/uwnd.' + str(year) + '.nc'
	data = [airTemp_surface,airTemp_midLevels, zonal_surface, zonal_midLevels]
	for filename in data:
		print("\n Downloading " + filename)
		wget.download(filename, out = outPath)
	return [year,month,date]

downloadData()