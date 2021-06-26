import os

def clean():
	datasets = 'datasets/'
	dailyProfiles_imgs = 'finalOutput_plots/dailyProfiles'
	dailyChanges_imgs = 'finalOutput_plots/deltaProfiles'
	temp3d = 'finalOutput_plots/airTemperature_3dSurfacePlots'
	npys = 'outData/'
	foldersMain = [datasets, dailyProfiles_imgs, dailyChanges_imgs, temp3d, npys]
	for item in foldersMain:
		for removal in os.listdir(item):
			os.remove(os.path.join(item,removal))
	try:
		os.remove("globalMap.png")
	except:
		pass