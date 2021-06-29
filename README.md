
## autoClim: Modern Climate Events - Automated Tropospheric Global Profiles

<p align="center"><img src=https://user-images.githubusercontent.com/47943744/123750937-c550b800-d8d4-11eb-80f9-58d768010fd0.jpeg alt=autoClim_logo width="300" height="300" align="middle"></p>


*autoClim  is currently undergoing a significant change in the variables offered, so this README may not provide a complete picture of the system's capabilities*  

This project looks to create a framework that allows a user to develop a list of useful atmospheric profiles automatically, when given a date. As of now, air temperature, zonal wind, and meridional wind are the only quantities considered. The system outputs a series of plots describing the week's events and changes in key variables. We use [NOAA's NCEP/NCAR pressure reanalysis](https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html) data as our primary input. All variables are evaluated at 3 altitudes: near-surface, the 850 mbar pressure level, and the 250 mbar pressure level. 

- The data is presented as an air temperature heatmap, under a quiver plot using zonal and meridional wind as x and y vector components, respectively. They both lie over a global outline map with country borders.
- We have three major output categories (samples in **finalOutput_plots/**): 
  - *dailyProfiles/* : Looks at each day's wind-temperature profile at all 3 altitudes. 
  - *deltaProfiles/*: Changes in wind-temperature profiles across different days, at all 3 altitudes.
  - *airTemperature_3dSurfacePlots/*: 3d surface plots highlighting air temperature profiles across different days, at all 3 altitudes.
- The program uses a date as input (after 1948), while the week's (plus minus 3 days) profiles act as output.
  - eg. for an input of November 7, 2020, the program outputs profiles from the 4th to the 10th, inclusive.
- Sample output is currently centered on **November 7, 2020**
- Datasets (used for sample output) handled by the *downloadData()* function in **pullData.py** have not been added to the repository. For the sake of maintaining a clean directory structure, an empty stand-in text file has been added to their target folder.
- Execute *runMain.py* to create your own profiles! (Python 3.7)

### Dependencies:
- **numpy 1.19.5**: Primary module used for data handling throughout the project.
- **Matplotlib 3.3.4**: Used to present results graphically.
- **netCDF4 1.5.2**: Used as a handler for .nc file input.
- **Cartopy 0.19.2**: Provides a global basemap.
- **wget 3.2.0**: Web interfacing to automate dataset downloads.
- **os**: Handles internal directory structure.
- **PIL 1.1.6**: Setting up the basemap usage in plots.



**Here's some of our output!**

![temperature_day4_250mbar](https://user-images.githubusercontent.com/47943744/120197959-3867ff80-c23f-11eb-8f78-15a9741785f6.png)
![day5_850mbar](https://user-images.githubusercontent.com/47943744/118973513-61f77000-b98f-11eb-9cfd-89eff3742d0e.png)
![day2to3_250mbar](https://user-images.githubusercontent.com/47943744/118972273-0082d180-b98e-11eb-90d9-c855b542ae36.png)
