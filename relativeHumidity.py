import numpy as np
from netCDF4 import Dataset
from matplotlib import pyplot as plt
from PIL import Image

# Both datasets use an evenly spaced grid with a 2.5 deg. resolution. 
# Relative humidity, expressed as a percentage, indicates a present state of absolute humidity relative to a maximum humidity given the same temperature.
# Levels (kPa) --> {1000,925,850,700,600,500,400,300} --> doesn't go higher b/c of tropopause temp. inversion.

def generate_relHumidity_profs(year,month,date,monthConversion):
	NC_relHumidity_atSurface = Dataset('datasets/rhum.sig995.' + str(year) + '.nc', "r", format="NETCDF4")
	NC_relHumidity_multiLevels = Dataset('datasets/rhum.' + str(year) + '.nc', "r", format="NETCDF4")
	relHumidity_surf = np.array(NC_relHumidity_atSurface.variables['rhum'])#	shape(366,73,144) for 2020.
	relHumidity = np.array(NC_relHumidity_multiLevels.variables['rhum'])#	shape(366,8,73,144) for 2020.
	# newDate calculation.
	if len(relHumidity) == 366: # Assuming no. of time entries for surf + pressure datasets are equal.
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
	relHumidity = np.rot90(relHumidity,1) # shape (8,366,73,144)
	relHumidity_at300 = relHumidity[-1][newDate - 3:newDate + 4]
	relHumidity_at850 = relHumidity[2][newDate - 3:newDate + 4] # Final shapes (7,73,144)
	relHumidity_surf = relHumidity_surf[newDate - 3:newDate + 4]
	full_relHumidity = np.array([relHumidity_surf,relHumidity_at850,relHumidity_at300])
	np.save("outData/rhum_7d_3l_3x7x73x144.npy",full_relHumidity) # Arranged by ascending altitude.
	return 0.

def plot_relHumidity(err):
	rhumData = np.load("outData/rhum_7d_3l_3x7x73x144.npy")
	rhumData = np.rot90(rhumData,1) # Switch primary looping var. to day
	# new shape(7,3,73,144).
	im = Image.open("globalMap.png")
	dayLabel = 1
	levelLabel = ['_atSurface','_850mbar','_300mbar']
	for day in rhumData:
		index_levelLabel = 0
		for level in day:
			fig = plt.figure()
			ax = plt.axes()
			plt.imshow(im,extent=[0,144,0,73])
			plt.xlabel("Latitude")
			plt.ylabel("Latitude")
			cs =  ax.contourf(level,alpha=0.5)
			plt.colorbar(cs, ax=ax, label="Relative Humidity (%)", orientation='horizontal')
			plt.savefig("finalOutput_plots/relativeHumidity/relativeHumidity_day" + str(dayLabel) + levelLabel[index_levelLabel] + ".png")
			plt.cla()
			plt.clf()
			plt.close()
			index_levelLabel += 1
		dayLabel += 1
	return 0.