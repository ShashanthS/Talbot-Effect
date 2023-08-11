from diffractio import plt, sp, np, um, mm, degrees, num_max_processors
from diffractio.scalar_masks_X import Scalar_mask_X
from diffractio.scalar_masks_XZ import Scalar_mask_XZ
from diffractio.scalar_sources_X import Scalar_source_X
from diffractio.scalar_fields_XZ import Scalar_field_XZ
from diffractio.utils_multiprocessing import execute_multiprocessing

x = np.linspace(-150*mm, 150*mm, 1000)
z = np.linspace(-500*mm, 1000*mm, 1000)
wavelength = 6 * mm
#period = 40 * um
# z_talbot = 2 * period**2 / wavelength

SlitWidth=[6]

u0 = Scalar_source_X(x, wavelength)
u0.plane_wave(A=1)

for sw in SlitWidth:
    t = Scalar_mask_X(x, wavelength, n_background=1)
    t.ronchi_grating(x0 = 100, period = 20*mm, fill_factor=sw/20) 

    talbot_effect = Scalar_field_XZ(x, z, wavelength)
    talbot_effect.incident_field(u0 * t)
    talbot_effect.WPM(has_edges=False)

    talbot_effect.draw(kind='intensity', draw_borders=True, z_scale='mm')
    #plt.ylim(-150 * mm, 150 * um)
    plt.show()
