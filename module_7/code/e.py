"""
    Software Copyright License for non-commercial scientific research purposes.
    Please read carefully the following terms and conditions and any accompanying documentation before you download and/or use this script. 
    By downloading and/or using this script (including downloading, cloning, installing, and any other use of this github repository), you acknowledge that you have read these terms and conditions, understand them, and agree to be bound by them. 
    If you do not agree with these terms and conditions, you must not download and/or use the Model & Software. 
    Any infringement of the terms of this agreement will automatically terminate your rights under this License
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
