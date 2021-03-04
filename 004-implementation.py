import skimage.io as io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import matplotlib
from skimage.util import img_as_float
from skimage.transform import resize
import cmath
import numpy as np
from numpy import linalg as LA

image_size = (16, 16)
x = np.matrix([[complex(0.2, 0.4)],
               [complex(1.1, -0.6)],
               [complex(0.45, -0.34)],
               [complex(1.2, 1.4)],
               [complex(0.2, 0.4)],
               [complex(1.1, -0.6)],
               [complex(0.45, -0.34)],
               [complex(1.2, 1.4)],
               [complex(0.2, 0.4)],
               [complex(1.1, -0.6)],
               [complex(0.45, -0.34)],
               [complex(1.2, 1.4)],
               [complex(0.2, 0.4)],
               [complex(1.1, -0.6)],
               [complex(0.45, -0.34)],
               [complex(1.2, 1.4)]])


def read_and_preprocess(file_name):
    img = img_as_float(rgb2gray(io.imread(file_name)))
    img = resize(img, image_size, anti_aliasing=True)
    return img


def apply_MIMO(img):
    H = np.matrix(img)
    max_val = float(H.max()) + 1e-3
    H = H / max_val
    H = H.astype(np.cdouble)
    r = H * x
    H_ct = H.getH()
    Q1 = H * H_ct
    Q2 = H_ct * H
    D1, U = LA.eig(Q1)
    D2, V = LA.eig(Q2)
    D = np.sqrt(D1)
    xp = V.getH() * x
    rp = U.getH() * r

    return D, xp, rp


img = read_and_preprocess('images/trump.jpg')
D, xp, rp = apply_MIMO(img)

# print(D)