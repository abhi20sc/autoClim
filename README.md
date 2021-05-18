## Modern Climate Events: Automated Tropospheric Global Profiles

This project looks to create a framework that allows a user to develop a list of useful atmospheric profiles automatically, when given a date. As of now, air temperature, zonal wind, and meridional wind are the only quantities considered. The system outputs a series of plots describing the week's events, and the changes in considered variables over this timespan. We use [NOAA's NCEP/NCAR pressure reanalysis](https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html) data as our primary input. All variables are evaluated at 3 altitudes: near-surface, the 850 mbar pressure level, and the 250 mbar pressure level. 

- The data is presented as a contour plot of air temperature, under a quiver plot using zonal and meridional wind as x-y coordinates respectively. They both lie over a global land outline with country borders.
- The program uses a date as input (after 1948), while the week's (plus minus 3 days) profiles act as output.
  - eg. for an input of November 7, 2020, the program outputs profiles from the 4th to the 10th, inclusive.
- Sample output for daily profiles can be found under **finalOutput_plots/dailyProfile** with appropriate filenames. 
- Sample output is currently centered on **November 7, 2020**
- Datasets (used for sample output) handled by the *downloadData()* function in **pullData.py** have not been added to the repository. For the sake of maintaining a clean directory structure, an empty stand-in text file has been added to their target folder.

### Dependencies:
- **numpy 1.19.5**: Primary module used for data handling throughout the project.
- **Matplotlib 3.3.4**: Used to present results graphically.
- **netCDF4 1.5.2**: Used as a handler for .nc file input.
- **Cartopy 0.19.2**: Provides a global basemap.
- **wget 3.2.0**: Web interfacing to automate dataset downloads.
- **os**: Handles internal directory structure.
- **PIL 1.1.6**: Setting up the basemap usage in plots.
