"""

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import numpy as np

from scipy.cluster.vq import kmeans, whiten

import matplotlib.pyplot as plt

def some_complex_function():
    features  = np.array([[ 1.9,2.3],

                        [ 1.5,2.5],

                        [ 0.8,0.6],

                        [ 0.4,1.8],

                        [ 0.1,0.1],

                        [ 0.2,1.8],

                        [ 2.0,0.5],

                        [ 0.3,1.5],

                        [ 1.0,1.0]])

    whitened = whiten(features)

    book = np.array((whitened[0],whitened[2]))

    return kmeans(whitened,book)

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
