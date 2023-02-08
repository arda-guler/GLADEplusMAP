# GLADE+MAP

![GLADE+MAP](https://user-images.githubusercontent.com/80536083/217591252-163c6596-a646-4883-9b0c-1922e0f95b87.jpg)

## About
Creates a 3D map of galaxies using data from GLADE+ catalog. The catalog from which the galaxy data is fetched is not my work - it is published as [1] and explained in detail at http://glade.elte.hu/.

## Obtaining the GLADE+ Catalog
The full catalog has not been uploaded to GitHub since the file size of the entire file is 6GB+. The copy in the data/ directory only includes the first 25,000 entries. To use the full catalog, you must replace 
data/GLADEplus.txt with the one you can download using the following link: http://elysium.elte.hu/~dalyag/GLADE+.txt

The Python script is sensitive to filename, so make sure that once you obtain the catalog, you rename it GLADEplus.txt or change the relevant line in loader.py.

## Using The Map
The map origin is marked with the intersection of three lines; red, green and blue. The red line shows the cartesian x axis, the green one the y axis, and the blue one the z axis. Each of these lines are 1 Mpa long. 

The right ascension (ra), declination (dec) and luminosity distance (d_L) values were used to compute the cartesian position vectors of galaxies as such:

x = d_L * cos(dec) * cos(ra)
y = d_L * cos(dec) * sin(ra)
z = d_L * sin(dec)

Color of each galaxy shows its mass. The color scale is a linear scale that paints the galaxy with the smallest mass as red, the galaxy with the largest mass as blue. All other galaxies are painted as a linear interpolation between fully blue and fully red, with zero green value in the RGB coloring scheme. The numerical value for maximum and minimum masses are displayed as the map generation is finished.

QWEASD keys control map camera rotation, UIOJKL keys control map camera position. T increases camera movement speed, G decreases it.

## IMPORTANT: Citation
Using any data or graphics from this map means that you have made use of data published in [1], which you must cite as described in https://arxiv.org/abs/2110.06184.

## References
[1] G Dálya, R Díaz, F R Bouchet, Z Frei, J Jasche, G Lavaux, R Macas, S Mukherjee, M Palfi, R S de~Souza, B D Wandelt, M Bilicki, & P Raffai (2022). GLADE+: an extended galaxy catalogue for multimessenger searches with advanced gravitational-wave detectors. Monthly Notices of the Royal Astronomical Society, 514(1), 1403–1411.  
