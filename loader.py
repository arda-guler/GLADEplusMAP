import pandas as pd
import math

from galaxy import *
from math_utils import *

# num. of galaxies = 23181757
def read_data(n="100"):

    # nothing given by user, default to load 50,000 galaxies from start
    if not n:
        n = "50000"

    # two values separated by comma
    if "," in n:
        n = eval("(" + n + ")")
        m = n[1]
        n = n[0]

        print("Reading galaxies between GLADE index", str(n), "to", str(m) + "...")
        data = pd.read_csv("data/GLADEplus.txt",
                           delimiter = ' ',
                           usecols = [0, 1, 2, 3, 4, 5, 6, 8, 9, 32, 35],
                           header = None,
                           names = ["GLADE", "PGC", "GWGC", "HyperLEDA", "2MASS", "WISExSCOS", "SDSS-DR16Q", "RA", "DEC", "d_L", "M*"],
                           low_memory = False,
                           skiprows = n,
                           nrows = (m-n))
        
    # all galaxies requested, good luck supercomputer
    elif n.lower() == "all":

        print("Reading all galaxies present in the GLADE+ catalogue...")
        data = pd.read_csv("data/GLADEplus.txt",
                           delimiter = ' ',
                           usecols = [0, 1, 2, 3, 4, 5, 6, 8, 9, 32, 35],
                           header = None,
                           names = ["GLADE", "PGC", "GWGC", "HyperLEDA", "2MASS", "WISExSCOS", "SDSS-DR16Q", "RA", "DEC", "d_L", "M*"],
                           low_memory = False)

    # n galaxies from top
    else:
        n = int(n)

        print("Reading the first", str(n), "galaxies in the GLADE+ catalogue...")
        data = pd.read_csv("data/GLADEplus.txt",
                           delimiter = ' ',
                           usecols = [0, 1, 2, 3, 4, 5, 6, 8, 9, 32, 35],
                           header = None,
                           names = ["GLADE", "PGC", "GWGC", "HyperLEDA", "2MASS", "WISExSCOS", "SDSS-DR16Q", "RA", "DEC", "d_L", "M*"],
                           low_memory = False,
                           nrows=n)

    return_data = data.to_dict('records')

    return return_data

def generate_galaxies(data):
    galaxies = []
    max_mass = 0
    min_mass = 2**16
    
    for row in data:
        pos = vec3(lst=spherical2cartesian([row["d_L"], row["RA"], row["DEC"]]))
        new_galaxy = galaxy(row["GLADE"], row["PGC"], row["GWGC"], row["HyperLEDA"], row["2MASS"], row["WISExSCOS"], row["SDSS-DR16Q"],
                            row["RA"], row["DEC"], row["d_L"], row["M*"], pos)
        galaxies.append(new_galaxy)
        
        if (not max_mass or new_galaxy.M > max_mass) and (not math.isnan(new_galaxy.M)):
            max_mass = new_galaxy.M

        if (not min_mass or new_galaxy.M < min_mass) and (not math.isnan(new_galaxy.M)):
            min_mass = new_galaxy.M

    return galaxies, min_mass, max_mass

        
        
