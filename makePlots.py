from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

def make_daily_windT_plots(err):
	# Loading data + setting up aux. iteration variables.
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
			base.append(newWeekly[int(e)][::2,::2])
		week.append(base)
	week = np.array(week)
	# Open basemap + setting up variables used in plots
	im = Image.open("globalMap.png")
	dayTitleCount = 1 #Used for filenames
	x = np.linspace(0,71,num=9,endpoint=True) # X-axis range
	xLabels = [str(i) for i in list(np.arange(start=-180,stop=181,step=45))] # X-axis range labels
	y = np.linspace(0,37,num=7,endpoint=True) # Y-axis range
	yLabels = [str(i) for i in list(np.arange(start=-90,stop=91,step=30))] # Y-axis range labels
	for day in week: 
		restructuredDay = day.reshape(3,3,37,72) # Reshapes to group by level for each qty.
		levelTitleCount = 0 # Used for filenames 
		for level in restructuredDay: # Loops through altitudes in one day.
			airT, uwnd, vwnd = level[0], level[1], level[2]
			fig = plt.figure()
			ax = plt.axes()
			plt.imshow(im,extent=[0,71,0,180/5]) # Extent adjusts for data sizes.
			plt.xlabel("Longitude")
			plt.ylabel("Latitude")
			plt.xticks(x,xLabels)
			plt.yticks(y,yLabels)
			cs = ax.contourf(airT,alpha=0.6)
			plt.colorbar(cs, ax=ax, label="Air Temperature (deg C)", orientation="horizontal")
			plt.quiver(uwnd,vwnd,color='red',alpha=0.6)
			plt.savefig('finalOutput_plots/dailyProfiles/day' + str(dayTitleCount) + titles[levelTitleCount])
			plt.cla() # Close ax w/colorbar
			plt.clf() # Close figure for data
			plt.close() # Remove image
			levelTitleCount += 1 #49+50: Increment filename variables
		dayTitleCount += 1
	return 0

def make_delta_windT_plots(err):
	# Loading data + setting up filename variables
	diffDataMain = np.load('outData/windT_delta_3x3qtyDiff-2dSpatial_profiles_3x3x6x73x144_.npy')
	titles = ['at_Surface','_250mbar','_850mbar']
	# See make_daily_plots() for lines 58-62 (inc.)
	im = Image.open("globalMap.png") 
	x = np.linspace(0,71,num=9,endpoint=True) 
	xLabels = [str(i) for i in list(np.arange(start=-180,stop=181,step=45))]
	y = np.linspace(0,37,num=7,endpoint=True)
	yLabels = [str(i) for i in list(np.arange(start=-90,stop=91,step=30))]
	# 3x3 5d into 9 4d [breaks down altitude grouping]
	diffDataMain = diffDataMain.reshape(9,6,73,144)
	# Make time the primary looping variable
	diffDataMain = np.rot90(diffDataMain) # new shape (6,9,73,144)
	# Rebuild altitude grouping
	diffDataMain = diffDataMain.reshape(6,3,3,73,144)
	# Final structure: time x qty x level x 2d spatial
	dayTitleCount = 1 
	for day in diffDataMain:
		# Change secondary looping variable to alt -> profiles made combining 3 qtys at 1 level
		day = np.rot90(day)
		levelTitleCount = 0
		for level in day:
			airT, uwnd, vwnd = level[0], level[1], level[2]
			airT = airT[::2,::2] # Resolution of 2
			uwnd = uwnd[::2,::2]
			vwnd = vwnd[::2,::2]
			fig = plt.figure()
			ax = plt.axes()
			cs = ax.contourf(range(72),range(37),airT,alpha=0.6)
			plt.imshow(im,extent=[0,71,0,180/5])
			plt.xlabel("Longitude")
			plt.ylabel("Latitude")
			plt.xticks(x,xLabels)
			plt.yticks(y,yLabels)
			plt.colorbar(cs,ax=ax,use_gridspec=False,label="Change in Air Temperature",orientation='horizontal')
			plt.quiver(uwnd,vwnd,color='red',alpha=0.6)
			plt.savefig('finalOutput_plots/deltaProfiles/day' + str(dayTitleCount) 
				+ "to" + str(dayTitleCount + 1) + titles[levelTitleCount])
			plt.clf()
			plt.cla()
			plt.close(fig)
			levelTitleCount += 1
		dayTitleCount += 1
	return 0