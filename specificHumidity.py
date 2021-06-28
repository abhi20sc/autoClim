import numpy as np
from netCDF4 import Dataset
from matplotlib import pyplot as plt
from PIL import Image

# Both datasets use an evenly spaced grid with a 2.5 deg. resolution.
# Relative humidity, expressed as a percentage, indicates a present state of absolute humidity relative to a maximum humidity given the same temperature.
# Levels (kPa) --> {1000,925,850,700,600,500,400,300} --> doesn't go higher b/c of tropopause temp. inversion.

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

def generate_specHumidity_profs(year,month,date,monthConversion):
	NC_specHumidity_2m = Dataset('datasets/shum.2m.gauss.' + str(year) + '.nc', "r", format="NETCDF4")
	NC_specHumidity_multiLevels = Dataset('datasets/shum.' + str(year) + '.nc', "r", format="NETCDF4")
	specHumidity_2m = np.array(NC_specHumidity_2m.variables['shum'])#	shape(366,94,192) for 2020.
	specHumidity = np.array(NC_specHumidity_multiLevels.variables['shum'])#	shape(366,8,73,144) for 2020.
	# newDate calculation.
	if len(specHumidity) == 366: # Assuming no. of time entries for surf + pressure datasets are equal.
		leapYear = True
	newDate = 0
	for elem in monthConversion.keys():
		if elem != month:
			newDate += (monthConversion[elem])[1]
		else:
			newDate += date
			break
	if leapYear == True and newDate > 59:
		newDate += 1
	# Extracting profs by alt. (Indexes: 300mbar: -1, 850mbar: 2)
	specHumidity = np.rot90(specHumidity,1) # shape (8,366,73,144)
	specHumidity_at300 = specHumidity[-1][newDate - 3:newDate + 4]
	specHumidity_at850 = specHumidity[2][newDate - 3:newDate + 4] # Final shapes (7,73,144)
	specHumidity_2m = specHumidity_2m[newDate - 3:newDate + 4]
	specHumidity = np.array([specHumidity_at850,specHumidity_at300])
	np.save("outData/shum_7d_3l_2x7x73x144.npy",specHumidity) # Arranged by ascending altitude.
	np.save("outData/shum_surf2m_7x94x192.npy",specHumidity_2m)
	return 0.

def plot_specHumidity(err):
	shumData = np.load("outData/shum_7d_3l_2x7x73x144.npy")
	shumSurfData = np.load("outData/shum_surf2m_7x94x192.npy")
	shumData = np.rot90(shumData,1) # Switch primary looping var. to day
	# new shape(7,2,73,144). --> shumData
	im = Image.open("globalMap.png")
	dayLabel = 1
	levelLabel = ['_850mbar','_300mbar']
	for day in shumData:
		index_levelLabel = 0
		for level in day:
			fig = plt.figure()
			ax = plt.axes()
			plt.imshow(im,extent=[0,144,0,73])
			plt.xlabel("Longitude")
			plt.ylabel("Latitude")
			cs =  ax.contourf(level,alpha=0.5)
			plt.colorbar(cs, ax=ax, label="Specific Humidity (kg/kg)", orientation='horizontal')
			plt.savefig("finalOutput_plots/specificHumidity/specificHumidity_day" + str(dayLabel) + levelLabel[index_levelLabel] + ".png")
			plt.cla()
			plt.clf()
			plt.close()
			index_levelLabel += 1
		dayLabel += 1
	# Creating surface profiles (shumSurfData)
	dayLabel = 1
	for day in shumSurfData:
		fig = plt.figure()
		ax = plt.axes()
		plt.imshow(im,extent=[0,192,0,94])
		plt.xlabel("Longitude")
		plt.ylabel("Latitude")
		cs = ax.contourf(day, alpha=0.5)
		plt.colorbar(cs, ax=ax, label="Specific Humidity (kg/kg)", orientation='horizontal')
		plt.savefig("finalOutput_plots/specificHumidity/specificHumidity_day" + str(dayLabel) + "_atSurface.png")
		plt.cla()
		plt.clf()
		plt.close()
		dayLabel += 1
	return 0.

# T62 grid error holds true for shumSurfData.