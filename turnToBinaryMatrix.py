import numpy as np

def turnToBinaryMatrix(M):
    """ Function replaces the non-zero elements in M with a 1
    """
    nonZero = np.flatnonzero(M)
    np.put(M, nonZero, 1)
    return M
