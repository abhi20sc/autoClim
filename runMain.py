from pullData import *
from genProfiles import *
from makePlots import *
from createGlobalMap import *
from cleanup import *
from matplotlib import pyplot as plt
import numpy as np
from netCDF4 import Dataset

def main():
	year, month, date = 2020,"November",7 # --> to be replaced with -- year, month, date, monthConversion = getDates()
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
	# clean() --> Remove comment to delete all sample data + datasets.
	#downloadData(year) # Comment out if datasets downloaded
	generate_daily_profs(year,month,date,monthConversion)
	diffs_gen()
	createGlobalMap()
	make_daily_plots()

	

if __name__ == "__main__":
	main()