from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

def make_daily_plots():
	weeklyPlotsMain = np.load("outData/9qty-7day-2dSpatial_profiles_9x7x73x144_.npy")
	titles = ['at_Surface','_250mbar','_850mbar']
	basic = np.linspace(-1,62,9,endpoint=False)
	week = []#np.empty((7,9))
	newWeekly = weeklyPlotsMain.reshape(63,73,144)
	for i in range(7):
		basic = [e + 1 for e in basic]
		base = []
		for e in basic:
			base.append(newWeekly[int(e)][::2,::2])
		week.append(base)
	week = np.array(week)
	im = Image.open("globalMap.png")
	dayTitleCount = 1
	x = np.linspace(0,71,num=9,endpoint=True)
	xLabels = [str(i) for i in list(np.arange(start=-180,stop=181,step=45))]
	y = np.linspace(0,37,num=7,endpoint=True)
	yLabels = [str(i) for i in list(np.arange(start=-90,stop=91,step=30))]
	for day in week:
		restructuredDay = day.reshape(3,3,37,72)
		levelTitleCount = 0
		for level in restructuredDay:
			airT, uwnd, vwnd = level[0], level[1], level[2]
			print(airT.max())
			fig = plt.figure()
			ax = plt.axes()
			plt.imshow(im,extent=[0,71,0,180/5])
			plt.xlabel("Longitude")
			plt.ylabel("Latitude")
			plt.xticks(x,xLabels)
			plt.yticks(y,yLabels)
			ax.contourf(airT,alpha=0.4)
			plt.colorbar(ax=ax, label="Air Temperature", orientation="horizontal")
			plt.quiver(uwnd,vwnd,color='red',alpha=0.4)
			plt.savefig('finalOutput_plots/dailyProfiles/day' + str(dayTitleCount) + titles[levelTitleCount])
			plt.clf()
			levelTitleCount += 1
		dayTitleCount += 1
	return 0