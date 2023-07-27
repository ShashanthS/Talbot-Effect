# -- coding: utf-8 --
"""
Created on Sun Dec 25 11:04:43 2022

@author: Mahathi
"""

import matplotlib.pyplot as plt
import diffractio
from diffractio import mm, np, degrees
from diffractio.scalar_sources_X import Scalar_source_X
from diffractio.scalar_masks_XZ import Scalar_mask_XZ
from diffractio.scalar_masks_X import Scalar_mask_X


# These lists define the thicknesses and slit widths to iterate throug
# Each slit width will be simulated using each value of grating thickness

thickness = [3, 6, 9, 12, 15, 18]
SlitWidth = [6, 9, 12, 14]
wavelength = 6*mm

x = np.linspace(-150*mm, 150*mm, 1000)
z = np.linspace(0, 300*mm, 1000)


u1 = Scalar_source_X(x=x, wavelength=wavelength)
u1.plane_wave(theta=0*degrees,z0=0*mm)
t0 = Scalar_mask_X(x=x, wavelength=wavelength)

for sw in SlitWidth:
    for t in thickness:        
        #t0.double_slit(x0 = 0, size=12mm, separation=20mm)
        t0.ronchi_grating(x0 = 0, period = 20*mm, fill_factor=sw/20) #period defines grating spacing and fill factor is the ratio of width to period

        t1 = Scalar_mask_XZ(x=x, z=z, wavelength=wavelength, n_background=1)

        z0 = (24-t)*mm #position of grating
        z1 = 24*mm #defines grating width
        v_globals = dict(z0=z0, z1=z1)

        t1.extrude_mask(t=t0, z0=z0, z1=z1, refraction_index=0, v_globals=v_globals)

        #t1.draw_refraction_index(draw_borders=True)

        t1.incident_field(u1)

        t1.WPM(has_edges=False)

        # Comment below out to disable intensity map
        t1.draw(kind='intensity', draw_borders=True, z_scale='mm')
        #plt.savefig(f'0_{sw}_{t}intensity.png')

        # Comment below out to disable phase map
        t1.draw(kind='phase', draw_borders=True, percentage_intensity=0, z_scale='mm')
        plt.ylabel('Temp')
        #plt.savefig(f'0_{sw}_{t}phase.png')
        plt.show()
