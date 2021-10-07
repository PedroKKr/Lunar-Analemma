from time import perf_counter

import numpy as np
import matplotlib.pyplot as plt

from astropy.coordinates.erfa_astrom import erfa_astrom, ErfaAstromInterpolator
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, get_moon, get_icrs_coordinates
from astropy.time import Time
import astropy.units as u
from time import sleep
from dynplot import dynplot

# 100_000 times randomly distributed over 12 hours
t = Time('2021-10-11T13:27:00')

location = EarthLocation(
    lon=-54.571257 * u.deg, lat=-20.439979 * u.deg, height=600 * u.m
)


dplt = dynplot()
dplt.ax.set_xlim(55, 130)
dplt.ax.set_ylim(-25,15)
for n in range(310):
    altt = []
    azz = []
    for i in range(28):
        # A celestial object in ICRS
        moon = get_moon(t,location)

        # target horizontal coordinate frame
        altaz = AltAz(obstime=t, location=location)

        altt.append(moon.transform_to(altaz).alt.deg)
        azz.append(moon.transform_to(altaz).az.deg)
        t += 24.8411996828*u.hour
    plt.title(str(t))
    dplt.plot(azz, altt)
    path = 'analemmas/fig'+str(n)+'.png'
    plt.savefig(path,dpi=300)
    dplt.show()

