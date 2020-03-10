import mrcfile as mrc
import matplotlib.pyplot as plt
import numpy as np

m0 = '0_0.mrcs'
m1 = '0_1.mrcs'
m2 = '0_2.mrcs'
m3 = '0_3.mrcs'
m4 = '0_4.mrcs'
ms = [m0,m1,m2,m3,m4]
ims = np.array([])
for m in ms:
    with mrc.open(m) as f:
        im = f.data
        flat = np.zeros((im.shape[0],1))
        for x in range(im.shape[0]):
            flat[x] = np.sum(im[x])
        flat = flat**2 / 9000
        if ims.size == 0:
            ims = im
        else:
            ims = np.hstack((ims,im))
        ims = np.hstack((ims,flat))
        ims = np.hstack((ims,flat))
        ims = np.hstack((ims,flat))
ims = ims**0.7

# fig, axs = plt.subplots(1, 5)
# axs[0].imshow(ims[0:150])
# axs[0].axis('off')
# axs[1].imshow(ims[150:300])
# axs[1].axis('off')
# axs[2].imshow(ims[300:450])
# axs[2].axis('off')
# axs[3].imshow(ims[450:600])
# axs[3].axis('off')
# axs[4].imshow(ims[600:750])
# axs[4].axis('off')
# plt.show()
plt.figure(2)
plt.imshow(ims, cmap='gray_r')
plt.axis('off')
# plt.show()
plt.savefig('common_line.png',bbox_inches='tight', pad_inches=0)
