import cartopy.crs as ccrs
import cartopy.feature as cf
from matplotlib import pyplot as plt
from matplotlib import image as img

def createMap():
	fig = plt.figure()
	ax = plt.axes(projection=ccrs.PlateCarree())
	ax.coastlines(linewidth=1)
	ax.add_feature(cf.BORDERS,linestyle='-',linewidth=1)
	plt.show()
	fig.savefig('globalMap.png', bbox_inches='tight', pad_inches=0)
	return 0.