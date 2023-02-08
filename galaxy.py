class galaxy:
    def __init__(self, idx_glade, idx_pgc, idx_gwgc, idx_hyperleda,
                 idx_2mass, idx_wisexscos, idx_sdssdr16q, ra, dec,
                 d_L, M, pos):
        
        self.idx_glade = idx_glade
        self.idx_pgc = idx_pgc
        self.idx_gwgc = idx_gwgc
        self.idx_hyperleda = idx_hyperleda
        self.idx_2mass = idx_2mass
        self.idx_wisexscos = idx_wisexscos
        self.isx_sdssdr16q = idx_sdssdr16q
        self.ra = ra # right ascension in deg
        self.dec = dec # declination in deg
        self.d_L = d_L # luminosity distance in Mpa
        self.M = M # stellar mass in 10^10 M_Sun units
        
        self.pos = pos # cartezian position vector in Mpa
