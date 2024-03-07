"""This script is modified from [code_sample](https://github.com/vujosp/code_scan_sample/blob/main/module_6/code/a.py).

Original license please see docs/additional_licenses.md.
"""

import numpy as np

from scipy.cluster.vq import kmeans, whiten

import matplotlib.pyplot as plt

def some_additional_functions():
    pts = 50

    rng = np.random.default_rng()

    a = rng.multivariate_normal([0, 0], [[4, 1], [1, 4]], size=pts)

    b = rng.multivariate_normal([30, 10],

                                [[10, 2], [2, 1]],

                                size=pts)

    features = np.concatenate((a, b))

    # Whiten data

    whitened = whiten(features)

    # Find 2 clusters in the data

    codebook, distortion = kmeans(whitened, 2)

    # Plot whitened data and cluster centers in red

    plt.scatter(whitened[:, 0], whitened[:, 1])

    plt.scatter(codebook[:, 0], codebook[:, 1], c='r')

    plt.show()
