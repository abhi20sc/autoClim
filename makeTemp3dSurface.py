import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import matplotlib.cm as cm

def make_temp3d_dailyPlots(err):
	weeklyPlotsMain = np.load("outData/windT_9qty-7day-2dSpatial_profiles_9x7x73x144_.npy")
	titles = ['at_Surface','_250mbar','_850mbar']
	basic = np.linspace(-1,62,9,endpoint=False)
	week = []
	newWeekly = weeklyPlotsMain.reshape(63,73,144)
	# Iterates through weeklyPlotsMain w/ 9-step jumps; jumps to next
	# time entry of identical quantity
	for i in range(7):
		# Shifts index range by 1 for each new date.
		basic = [e + 1 for e in basic]
		base = []
		for e in basic:
			# Saving data with a resolution of 2
			base.append(newWeekly[int(e)])
		week.append(base)
	week = np.array(week)
	# Setting up variables used in plots
	dayTitleCount = 1 #Used for filenames
	yMain = np.linspace(0,144,num=9,endpoint=True) # X-axis range
	yLabels = [str(i) for i in list(np.arange(start=-180,stop=181,step=45))] # X-axis range labels
	xMain = np.linspace(0,73,num=7,endpoint=True) # Y-axis range
	xLabels = [str(i) for i in list(np.arange(start=-90,stop=91,step=30))] # Y-axis range labels
	for day in week: 
		day = day.reshape(3,3,73,144) # Reshapes to group by level for each qty.
		levelTitleCount = 0 # Used for filenames 
		day = day[:,0,:,:] # Extracts only airT data; Newshape (3,37,72)
		for airT in day:
			x = range(73)
			y = range(144)[::-1]
			x, y = np.meshgrid(x,y)
			fig = plt.figure(figsize=(8,6))
			ax = Axes3D(fig)
			surf = ax.plot_surface(x,y,np.transpose(airT), rstride=1, cstride=1, cmap='viridis')
			plt.xticks(xMain, xLabels)
			plt.yticks(yMain, yLabels)
			plt.xlabel("Latitude")
			plt.ylabel("Longitude")
			ax.set_zlabel("Air Temperature (K)")
			plt.gca().invert_xaxis()
			plt.savefig('finalOutput_plots/airTemperature_3dSurfacePlots/temperature_day' + str(dayTitleCount) + titles[levelTitleCount])
			plt.cla() # Close ax w/colorbar
			plt.clf() # Close figure for data
			plt.close() # Remove image
			levelTitleCount += 1 # Lines 49 + 50: Increment filename variables
		dayTitleCount += 1
	return 0
