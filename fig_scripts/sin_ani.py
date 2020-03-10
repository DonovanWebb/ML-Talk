import mrcfile as mrc
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from skimage.transform import radon, rescale
import math


im1 = '/dls/ebic/data/staff-scratch/Donovan/3Drepro/Radon/NN/proj_5angles/i0/0.mrc'
with mrc.open(im1) as f:
    img1 = f.data
    

def get_proj(im, angle, give_sino=False):
    rad_angle = angle/360 * 2*np.pi
    grid = np.zeros((im.shape[0],im.shape[1]))
    theta = np.linspace(0., 360., 360, endpoint=False)
    sinogram = radon(im, theta=theta, circle=True)
    if give_sino:
        return sinogram
    sinogram = sinogram.T
    center = im.shape[0] // 2
    for i in range(-center,center):
        x = center+math.sin(rad_angle)*i
        y = center+math.cos(rad_angle)*i

        grid[int(np.floor(x)),int(np.floor(y))] = sinogram[angle][center-i-1]
        grid[int(np.floor(x-0.3)),int(np.floor(y-0.3))] = sinogram[angle][center-i-1]
        grid[int(np.floor(x-0.3)),int(np.floor(y+0.3))] = sinogram[angle][center-i-1]
        grid[int(np.floor(x+0.3)),int(np.floor(y-0.3))] = sinogram[angle][center-i-1]
        grid[int(np.floor(x+0.3)),int(np.floor(y+0.3))] = sinogram[angle][center-i-1]
    return grid[10:-10,10:-10]


gridspec.GridSpec(5,3)

# Arrows
def tl(arrow=True):
    plt.subplot2grid((3,5), (0,0))
    if arrow:
        for i in range(2,7):
            plt.arrow(i/10,0.2+i/10,0.4,-0.4, capstyle='projecting',length_includes_head=True,head_width=0.05, head_length=0.1)
    else:
        plt.imshow(get_proj(img1,135),cmap='gray_r')
    plt.axis('off')
    return plt

def tm(arrow=True):
    plt.subplot2grid((3,5), (0,1))
    if arrow:
        for i in np.arange(10/6,10,10/6):
            plt.arrow(i/10,0.9,0,-0.56, capstyle='projecting',length_includes_head=True,head_width=0.05, head_length=0.1)
    else:
        plt.imshow(get_proj(img1,0),cmap='gray_r')
    plt.axis('off')

def tr(arrow=True):
    plt.subplot2grid((3,5), (0,2))
    if arrow:
        for i in range(2,7):
            plt.arrow(0.2+i/10,1-i/10,-0.4,-0.4, capstyle='projecting',length_includes_head=True,head_width=0.05, head_length=0.1)
    else:
        plt.imshow(get_proj(img1,45),cmap='gray_r')
    plt.axis('off')
    return plt

def ml(arrow=True):
    plt.subplot2grid((3,5), (1,0))
    if arrow:
        for i in np.arange(10/6,10,10/6):
            plt.arrow(0.1,i/10,0.56,0, capstyle='projecting',length_includes_head=True,head_width=0.05, head_length=0.1)
    else:
        plt.imshow(get_proj(img1,90),cmap='gray_r')
    plt.axis('off')
    return plt

def mr(arrow=True):
    plt.subplot2grid((3,5), (1,2))
    if arrow:
        for i in np.arange(10/6,10,10/6):
            plt.arrow(0.9,i/10,-0.56,0, capstyle='projecting',length_includes_head=True,head_width=0.05, head_length=0.1)
    else:
        plt.imshow(get_proj(img1,90),cmap='gray_r')
    plt.axis('off')
    return plt

def bl(arrow=True):
    plt.subplot2grid((3,5), (2,0))
    if arrow:
        for i in range(2,7):
            plt.arrow(1-(0.2+i/10),+i/10,+0.4,+0.4, capstyle='projecting',length_includes_head=True,head_width=0.05, head_length=0.1)
    else:
        plt.imshow(get_proj(img1,45),cmap='gray_r')
    plt.axis('off')
    return plt

def bm(arrow=True):
    plt.subplot2grid((3,5), (2,1))
    if arrow:
        for i in np.arange(10/6,10,10/6):
            plt.arrow(i/10,0.1,0,+0.56, capstyle='projecting',length_includes_head=True,head_width=0.05, head_length=0.1)
    else:
        plt.imshow(get_proj(img1,0),cmap='gray_r')
    plt.axis('off')
    return plt

def br(arrow=True):
    plt.subplot2grid((3,5), (2,2))
    if arrow:
        for i in range(2,7):
            plt.arrow(1-i/10,1-(0.2+i/10),-0.4,0.4, capstyle='projecting',length_includes_head=True,head_width=0.05, head_length=0.1)
    else:
        plt.imshow(get_proj(img1,135),cmap='gray_r')
    plt.axis('off')
    return plt


def always():
    # 2D proj
    # blank = np.zeros((10,10))
    # for i in range(3):
    #     for j in range(5):
    #         plt.subplot2grid((3,5), (i,j))
    #         plt.imshow(blank, cmap='gray_r')
    #         plt.axis('off')

    plt.subplot2grid((3,5), (1,1))
    plt.imshow(np.round(abs(img1),3), cmap='gray_r')
    plt.axis('off')

    return plt

def sino(angle,sin,new_sin=True, part_sino=True):
    # Sino
    sino_all = get_proj(img1,0,True)
    if not part_sino:
        sino_all[0,:] = 1000
        sino_all[-1,:] = 1000
        sino_all[:,0] = 1000
        sino_all[:,-1] = 1000
        plt.subplot2grid((3,5), (1,3), colspan=2)
        plt.imshow(sino_all, cmap='gray_r')
        plt.axis('off')
        return plt
    zeros = sin
    if new_sin:
        zeros = np.zeros((sino_all.shape[0],sino_all.shape[1]))
    zeros[:,angle-2:angle+2] = sino_all[:,angle-2:angle+2]
    zeros[0,:] = 1000
    zeros[-1,:] = 1000
    zeros[:,0] = 1000
    zeros[:,-1] = 1000

    plt.subplot2grid((3,5), (1,3), colspan=2)
    plt.imshow(zeros, cmap='gray_r')
    plt.axis('off')
    return plt, zeros


def animation():
    # 1
    always()
    plt.tight_layout()
    _, sin  =sino(3, 0)
    bm(False)
    tm()
    plt.savefig('sino_make_fr1.png')
    # 2
    always()
    plt.tight_layout()
    _,sin = sino(3,sin)
    bm(False)
    _,sin = sino(45,sin,False)
    bl(False)
    tr()
    plt.savefig('sino_make_fr2.png')
    # 3
    always()
    plt.tight_layout()
    _,sin = sino(3,sin)
    bm(False)
    _,sin = sino(45,sin,False)
    bl(False)
    _,sin = sino(90,sin,False)
    ml(False)
    mr()
    plt.savefig('sino_make_fr3.png')
    # 4
    always()
    plt.tight_layout()
    sino(0,sin, False,False)
    tl(False)
    tm(False)
    tr(False)
    ml(False)
    mr(False)
    bl(False)
    bm(False)
    br(False)
    plt.savefig('sino_make_fr4.png')


animation()
