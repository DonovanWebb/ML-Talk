import mrcfile as mrc
import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import radon, rescale



m0 = '/dls/ebic/data/staff-scratch/Donovan/3Drepro/Radon/NN/proj_5angles/i0/0.mrc'
m1 = '/dls/ebic/data/staff-scratch/Donovan/3Drepro/Radon/NN/proj_5angles/i0/1.mrc'
with mrc.open(m0) as f:
    im0 = f.data
with mrc.open(m1) as f:
    im1 = f.data

def sino(im):
    theta = np.linspace(0., 360., 360, endpoint=False)
    sinogram = radon(im, theta=theta, circle=True)
    return sinogram.T

sin0 = sino(im0)
sin1 = sino(im1)

matc = np.zeros((360,360))
matsq = np.zeros((360,360))
for a in range(360):
    l1 = sin0[a]
    l1_ = (l1 - np.mean(l1)) / (np.std(l1) * len(l1))
    for b in range(360):
        l2 = sin1[b]
        l2_ = (l2 - np.mean(l2)) / (np.std(l2))
        c = np.correlate(l1_, l2_, 'valid')
        sq = np.cbrt(((l1-l2)**2).mean(axis=0))
        matc[a,b] = c
        matsq[a,b] = sq


plt.figure(1)
plt.imshow(matc**4, cmap='gray')
plt.figure(2)
plt.imshow(matsq, cmap='gray_r')
plt.figure(3)
plt.plot(sin0[0])
plt.plot(sin0[20])
plt.show()


