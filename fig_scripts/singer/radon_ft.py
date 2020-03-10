import mrcfile as mrc
from skimage.transform import radon, rescale
import matplotlib.pyplot as plt
import numpy as np

im1 = '/dls/ebic/data/staff-scratch/Donovan/3Drepro/Radon/NN/proj_5angles/i0/0.mrc'
with mrc.open(im1) as f:
    img1 = f.data
theta = np.linspace(0., 180., 180, endpoint=False)
sinogram = radon(img1, theta=theta, circle=True)

import cv2

f = np.fft.fft2(img1)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))


plt.subplot(131),plt.imshow(img1, cmap = 'gray')
plt.title('Real Space'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(sinogram, cmap = 'gray')
plt.title('Radon Space'), plt.xticks(range(0,181,60)), plt.yticks([])
plt.xlabel('$\\theta$')
plt.subplot(133)
plt.imshow(magnitude_spectrum, cmap = 'gray')
sh = img1.shape[0]
plt.arrow(0.5*sh,0.5*sh,0.42*sh,0)
plt.arrow(0.5*sh,0.5*sh,0.3*sh,-0.3*sh)
plt.text(0.58*sh,0.49*sh,'$\\theta$', fontsize=12)
plt.title('Fourier Space'), plt.xticks([]), plt.yticks([])
plt.savefig('radon_ft.png',bbox_inches='tight', pad_inches=0)
plt.show()
