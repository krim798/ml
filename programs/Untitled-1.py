import numpy as np
def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    #Your code here
    n=int(input("Enter n:"))
    A=np.random.random([n,1])
    print("A =", A)
    return None
randomization()
