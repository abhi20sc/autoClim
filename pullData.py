Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@Mihir-DG 
Mihir-DG
/
autoClim
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
autoClim/pullData.py /
@Mihir-DG
Mihir-DG test: removed comments on pullData for new branch
Latest commit 8c443c0 17 hours ago
 History
 1 contributor
138 lines (132 sloc)  6.93 KB
  
import wget
import numpy as np
import os

def getDates():
	# Internal dictionary for validation calc.
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
	return [year,month,date,monthConversion]


def flatten_recursive(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten_recursive(item)
        else:
            yield item

def chooseData(year):
	avail = {
	1 : "Wind Vector Plot (Standard Heights) (overlaying air temperature contours)",
	2 : "Delta Profiles for (1) - changes across the chosen week.",
	3 : "Air Temperature at standard heights - 3d surface plots.",
	4 : "Precipitation Rate (Surface) - Heatmap",
	5 : "Relative Humidity (Standard Heights) - Heatmap",
	6 : "Specific Humidity (Standard Heights) - Heatmap",
	7 : "Aggregate Cloud Cover (EATM) - Heatmap",
	8 : "Skin Temperature (Surface)",
	9 : "Potential Temperature - Full Vertical Profile For Key Latitudes",
	10 : "Precitable Water (EATM) - Heatmap",
	11 : "Latent Heat Net Flux (Surface) - Heatmap",
	12 : "Sensible Heat Net Flux (Surface) - Heatmap",
	13 : "Ground Heat Net Flux (Surface) - Heatmap",
	14 : "Potential Evapotranspiration Rate (Surface) - Heatmap",
	15 : "Outgoing Longwave Radiation (OLR) - Heatmap",
	16 : "Upwelling Longwave Radiation (Surface) - Heatmap",
	17 : "Net Longwave Radiation (Surface) - Heatmap",
	18 : "Net Shortwave Radiation (Surface) - Heatmap",
	19 : "Tropopause Air Temperature - Heatmap",
	20 : "Tropopause Air Pressure - 3d Surface Plots",
	21 : "Lifted Index (Surface) - Heatmap"
	}
	for option in avail.keys():
		print(str(option) + ") " + avail[option])
	print("\n\n Enter the serial numbers of all the profiles you're interested in, one-by-one. Enter '0' when you're finished!")
	exit = False
	chosenData = []
	while exit == False:
		index = int(input())
		if index == 0 :
			exit = True
		else:
			chosenData.append(index)
	return chosenData

def downloadData(year,chosenData):
	ftpLinks = {
	1 : ["ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface/air.sig995." + str(year) + ".nc", 
			"ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/air." + str(year) + ".nc",
			'ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface/uwnd.sig995.' + str(year) + '.nc',
			'ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/uwnd.' + str(year) + '.nc',
			'ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface/vwnd.sig995.' + str(year) + '.nc',
			'ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/vwnd.' + str(year) + '.nc'],
	2 : ["ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface/air.sig995." + str(year) + ".nc", 
			"ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/air." + str(year) + ".nc",
			'ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface/uwnd.sig995.' + str(year) + '.nc',
			'ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/uwnd.' + str(year) + '.nc',
			'ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface/vwnd.sig995.' + str(year) + '.nc',
			'ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/vwnd.' + str(year) + '.nc'],
	3 : ["ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface/air.sig995." + str(year) + ".nc",
			"ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/air." + str(year) + ".nc"],
	4 : ["ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface_gauss/prate.sfc.gauss." + str(year) + '.nc'],
	5 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface/rhum.sig995.' + str(year) + '.nc',
			'ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/rhum.' + str(year) + '.nc'],
	6 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface_gauss/shum.2m.gauss.' + str(year) + '.nc',
			'ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/shum.' + str(year) + '.nc'],
	7 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/other_gauss/tcdc.eatm.gauss.' + str(year) + '.nc'],
	8 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface_gauss/skt.sfc.gauss.' + str(year) + '.nc'],
	9 : ["ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/pressure/air." + str(year) + ".nc"],
	10 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface/pr_wtr.eatm.' + str(year) + '.nc'],
	11 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface_gauss/lhtfl.sfc.gauss.' + str(year) + '.nc'],
	12 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface_gauss/shtfl.sfc.gauss.' + str(year) + '.nc'],
	13 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface_gauss/gflux.sfc.gauss.' + str(year) + '.nc'],
	14 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface_gauss/pevpr.sfc.gauss.' + str(year) + '.nc'],
	15 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/other_gauss/ulwrf.ntat.gauss.' + str(year) + '.nc'],
	16 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface_gauss/ulwrf.sfc.gauss.' + str(year) + '.nc'],
	17 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface_gauss/ulwrf.sfc.gauss.' + str(year) + '.nc'],
	18 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface_gauss/nswrs.sfc.gauss.' + str(year) + '.nc'],
	19 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/tropopause/air.tropp.' + str(year) + '.nc'],
	20 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/tropopause/pres.tropp.' + str(year) + '.nc'],
	21 : ['ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface/lftx4.sfc.' + str(year) + '.nc']
	}
	chosenFTPs = []
	for slNo in chosenData:
		chosenFTPs.append(ftpLinks[slNo]) # Add value from key index.
	chosenFTPs = list(flatten_recursive(chosenFTPs)) # Flatten chosenFTPs
	chosenFTPs = list(dict.fromkeys(chosenFTPs)) # Ensure no repetition in download list.
	# Clearing all older files from directory.
	outPath = 'datasets/'
	filelist = [ f for f in os.listdir(outPath)]
	for file in filelist:
		os.remove(os.path.join(outPath, file))
	# Downloading data.
	for filename in chosenFTPs:
		print("\n Downloading + " filename)
		wget.download(filename, out = 'datasets/')
	return 0.