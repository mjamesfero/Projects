import numpy as np
import pylab as pl

sigma_to_fwhm = np.sqrt(8*np.log(2))

def photometry_and_astrometry(image, star_center, cutout_width,
                              estimated_dark_current=4, background=None,
                              pixel_uncertainty_estimate=None,
                              threshold=2,
                              show_cutout=False,
                             ):
    # blyc = bottom-left y-coordinate
    # tryc = top-right y-coordinate
    blyc = star_center[0]-cutout_width[0]//2
    tryc = star_center[0]+cutout_width[0]//2
    blxc = star_center[1]-cutout_width[1]//2
    trxc = star_center[1]+cutout_width[1]//2
    star_cutout = image[blyc:tryc, blxc:trxc]
    
    # Key modification
    # image < 2*sigma
    star_cutout.mask[:] = star_cutout < threshold*pixel_uncertainty_estimate
    if show_cutout:
        pl.figure()
        pl.imshow(star_cutout)
        pl.colorbar()
    
    yc, xc = np.indices(star_cutout.shape)
    mom1_x = (xc * star_cutout).sum() / star_cutout.sum()
    mom1_y = (yc * star_cutout).sum() / star_cutout.sum()
    mom2_x = ((xc - mom1_x)**2 * star_cutout).sum() / star_cutout.sum()
    mom2_y = ((yc - mom1_y)**2 * star_cutout).sum() / star_cutout.sum()
    fwhm_x = mom2_x**0.5*sigma_to_fwhm
    fwhm_y = mom2_y**0.5*sigma_to_fwhm

    star_cutout_including_background = star_cutout + background + estimated_dark_current

    readnoise_squared = 100
    sigma_squared_F = star_cutout_including_background + readnoise_squared
    F = star_cutout

    sigma_squared_xi = ((sigma_squared_F * xc**2).sum() / F.sum()**2 +
                        (xc*F).sum()**2 * sigma_squared_F.sum() / F.sum()**4)
    sigma_squared_yi = ((sigma_squared_F * yc**2).sum() / F.sum()**2 +
                        (yc*F).sum()**2 * sigma_squared_F.sum() / F.sum()**4)
    mom1_x_uncertainty = sigma_squared_xi**0.5
    mom1_y_uncertainty = sigma_squared_yi**0.5
    
    total_flux = star_cutout.sum()
    total_flux_uncertainty = (star_cutout + pixel_uncertainty_estimate**2 + readnoise_squared).sum()**0.5
    
    # in the steps above, we wanted to _include_ the star.  Now, in the whole image, we want to _exclude_ it!
    star_cutout.mask[:] = ~star_cutout.mask
    
    # note that we want the coordinates in the original frame!
    return (total_flux, total_flux_uncertainty, mom1_x+blxc, mom1_y+blyc,
            mom1_x_uncertainty, mom1_y_uncertainty, fwhm_x, fwhm_y)
