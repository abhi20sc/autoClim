import numpy as np
from netCDF4 import Dataset
from PIL import Image
from matplotlib import pyplot as plt

def generate_precipitationRate_profs(year,month,date,monthConversion):
	NC_precipitationRate = Dataset("datasets/prate.sfc.gauss." + str(year) + ".nc","r",format="NETCDF4")
	prate = np.array(NC_precipitationRate.variables['prate'])
	# Month conversion to 365-day scale + leap year correction
	if len(prate) == 366:
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
	prate = prate[newDate-3:newDate+4]
	np.save("outData/prate_7day_surface_7x94x192",prate)
	return 0.

def plot_precipitationRate(err):
	prateData = np.load("outData/prate_7day_surface_7x94x192.npy")
	im = Image.open("globalMap.png")
	dayLabel = 1
	for dailyProfile in prateData:
		fig = plt.figure()
		ax = plt.axes()
		plt.imshow(im,extent=[0,192,0,94])
		plt.xlabel("Latitude")
		plt.ylabel("Latitude")
		cs =  ax.contourf(dailyProfile,alpha=0.6)
		plt.colorbar(cs, ax=ax, label="Precipitation Rate (Kg/m^2/s)", orientation='horizontal')
		plt.savefig("finalOutput_plots/precipitationDaily/precipitationRate_day" + str(dayLabel) + ".png")
		dayLabel += 1
		plt.cla()
		plt.clf()
		plt.close()

# Note: Currently, no attempt has been made to resolve the irregular latitudinal
#	spacing in the T62 gaussian grid setup --> have to come back to it later.