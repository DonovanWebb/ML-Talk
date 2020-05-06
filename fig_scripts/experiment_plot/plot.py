import numpy as np
import matplotlib.pyplot as plt


SNR = np.array([1000,1,1/2,1/3,1/4])
TSNE2C = np.array([4, 9.3, 24.3, 31.6, 46.3])
UMAP2C = np.array([1.3, 3, 6, 36, 62])
UMAP10C = np.array([2.7, 4, 4, 10.3, 31])


def plot_one(data, SNR, N, plt, label):
    data = (N-data)/N *100
    noise = 1/SNR
    plt.plot(noise, data, label=label)
    return plt

plt.figure(1)
plt = plot_one(TSNE2C, SNR, 160, plt, 'TSNE 2 components')
plt = plot_one(UMAP2C, SNR, 160, plt, 'UMAP 2 components')
plt = plot_one(UMAP10C, SNR, 160, plt, 'UMAP 10 components')
plt.xlabel('1/SNR')
plt.ylabel('% Correctly assigned')
plt.legend(loc="lower left")
plt.savefig('exp_plots.png', dpi=240)
