import numpy as np
from netCDF4 import Dataset

def generate_precipitationRate_profs(year,month,date,monthConversion):
	NC_precipitationRate = Dataset("datasets/prate.sfc.gauss." + str(year) + ".nc")
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
	print(prate.shape)
	np.save("outData/prate_7day_surface_7x94x192")
	return 0.
