import os

def clean():
	datasets = 'datasets/'
	dailyProfiles_imgs = 'finalOutput_plots/dailyProfiles'
	dailyChanges_imgs = 'finalOutput_plots/deltaProfiles'
	npys = 'outData/'
	foldersMain = [datasets, dailyProfiles_imgs, dailyChanges_imgs, npys]
	for dataset in os.listdir(datasets):
		os.remove(os.path.join(datasets,dataset))
	os.remove("globalMap.png")