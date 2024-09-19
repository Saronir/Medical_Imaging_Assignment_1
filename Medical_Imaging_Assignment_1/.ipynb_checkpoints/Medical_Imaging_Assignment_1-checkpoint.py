
from matplotlib.colors import LogNorm
import matplotlib.pyplot as pl
import numpy as np
import phantominator as ph
from scipy.fft import fftshift

#a
phantom = ph.shepp_logan(128)
pl.imshow(phantom)
pl.show()

#b
FT = np.fft.fft2(phantom)
FTS = fftshift(FT)
pl.imshow(np.real(FTS), vmin = 0, vmax = 255)
pl.show()
pl.imshow(np.imag(FTS), vmin = 0, vmax = 255)
pl.show()
pl.imshow(np.abs(FTS), vmin = 0, vmax = 255)
pl.show()

#c
FTdown = np.compress(FT)
IFT = np.fft.ifft2(FTdown)
pl.imshow(IFT)
pl.show()

