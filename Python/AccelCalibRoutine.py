__author__ = 'bsgiovanini'

from math import pow
import numpy as np
from numpy.linalg import inv


B = np.matrix([[.1], [.1], [.1]])


def init():
    pos0reader = np.loadtxt(open('dataPos0.txt', 'rb'), dtype=float, delimiter=';')
    pos1reader = np.loadtxt(open('dataPos1.txt', 'rb'), dtype=float, delimiter=';')
    pos2reader = np.loadtxt(open('dataPos2.txt', 'rb'), dtype=float, delimiter=';')
    pos3reader = np.loadtxt(open('dataPos3.txt', 'rb'), dtype=float, delimiter=';')
    pos4reader = np.loadtxt(open('dataPos4.txt', 'rb'), dtype=float, delimiter=';')
    pos5reader = np.loadtxt(open('dataPos5.txt', 'rb'), dtype=float, delimiter=';')

    #adxl_data = pos0reader

    data = np.concatenate((pos0reader, pos1reader, pos2reader, pos3reader, pos4reader, pos5reader))

    print gn(data)


def residual(x, y, z, B1, B2, B3):
    return 1 - pow(x - B1, 2) - pow(y - B2, 2) - pow(z - B3, 2)


def jacobian(v, B):
    return 2 * (v - B)


def gn(data):
    global B

    rows = len(data)

    J = np.zeros((rows, 3))
    r = np.zeros((rows, 1))

    for _ in xrange(50):

        for i in xrange(rows):
            r[i, 0] = residual(data[i, 0], data[i, 1], data[i, 2], B[0], B[1], B[2])
            J[i, 0] = jacobian(data[i, 0], B[0])
            J[i, 1] = jacobian(data[i, 1], B[1])
            J[i, 2] = jacobian(data[i, 2], B[2])

        Jt = J.T

        B = B - np.dot(np.dot(inv(np.dot(Jt, J)), Jt), r)


    print B

    for i in xrange(rows):
        print round(data[i, 0] - B[0], 2)
        print round(data[i, 1] - B[1], 2)
        print round(data[i, 2] - B[2], 2)


init()




