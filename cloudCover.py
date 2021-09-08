import numpy as np
from netCDF4 import Dataset
from PIL import Image
from matplotlib import pyplot as plt

def generate_cloudCover(year,month,date,monthConversion):
	cloudCover_rate = Dataset("datasets/crate.atms.gauss." + str(year) + ".nc","r",format="NETCDF4")
	crate = np.array(cloudCover_rate.variables['crate'])
	# Month conversion to 365-day scale + leap year correction
	if len(crate) == 366:
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
	crate = crate[newDate-3:newDate+4]
	np.save("outData/crate_7day_atms_7x94x192",crate)
	return 0.

def plot_cloudCover(err):
	crateData = np.load("outData/crate_7day_atms_7x94x192.npy")
	x = np.linspace(0,191,num=9,endpoint=True)
	xLabels = [str(i) for i in list(np.arange(start=-180,stop=181,step=45))]
	y = np.linspace(0,93,num=7,endpoint=True)
	yLabels = [str(i) for i in list(np.arange(start=-90,stop=91,step=30))]
	im = Image.open("globalMap.png")
	dayLabel = 1
	for dailyProfile in crateData:
		fig = plt.figure()
		ax = plt.axes()
		plt.imshow(im,extent=[0,191,0,93])
		plt.xlabel("Latitude")
		plt.ylabel("Latitude")
		plt.xticks(x,xLabels)
		plt.yticks(y,yLabels)
		cs =  ax.contourf(dailyProfile,alpha=0.6)
		plt.colorbar(cs, ax=ax, label="Cloud Cover Rate (%)", orientation='horizontal')
		plt.savefig("finalOutput_plots/cloudCoverRate/cloudCoverRate_day" + str(dayLabel) + ".png")
		dayLabel += 1
		plt.cla()
		plt.clf()
		plt.close()