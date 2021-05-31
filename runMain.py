from pullData import *
from genProfiles import *
from makePlots import *
from createGlobalMap import *
from cleanup import *
from makeTemp3dSurface import *
from matplotlib import pyplot as plt
import numpy as np
from netCDF4 import Dataset

def main():
	year, month, date, monthConversion = getDates()
	clean() # deletes all sample data + datasets.
	downloadData(year) # Comment out if datasets downloaded
	generate_daily_profs(year,month,date,monthConversion)
	diffs_gen()
	createGlobalMap()
	make_daily_plots()
	make_delta_plots()
	make_temp3d_dailyPlots()

if __name__ == "__main__":
	main()