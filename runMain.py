from pullData import *
from genProfiles import *
from makePlots import *
from createGlobalMap import *
from cleanup import *
from makeTemp3dSurface import *
from precipitationDat_prep import *

from matplotlib import pyplot as plt
import numpy as np
from netCDF4 import Dataset

def main():
	year, month, date, monthConversion = getDates() #
	a = input("Do you want all sample data and all datasets removed? Enter any character to stop their deletion")
	if a:
		clean() # deletes all sample data + datasets.
	downloadData(year) # Comment out if datasets downloaded
	createGlobalMap()
	try: 
		generate_daily_windT_profs(year,month,date,monthConversion) # Wind Quivers + Temp data 
		make_daily_windT_plots() # Plotting quivers/temp
		make_temp3d_dailyPlots() # plotting 3d surface temp profiles
		diffs_windT_gen() # calculating delta quiver/temps data
		make_delta_windT_plots() # creating delta quiver/temps plots
		

if __name__ == "__main__":
	main()