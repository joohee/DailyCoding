# http://cs231n.github.io/python-numpy-tutorial/

import numpy as np

class NumPyExample():
    def __init__(self):
        pass

    def example1(self):
        a = np.array([1, 2, 3])
        print ("type:", type(a))
        print("shpae:\n ", a.shape)
        print("a[0]: {0}, a[1]: {1}, a[2]: {2}".format(a[0], a[1], a[2]))
        a[0] = 5
        print("after changing value: ", a)

        b = np.array([[1,2,3],[4,5,6]])
        print("shape:", b.shape)
        print("b[0,0]: {}, b[0,1]: {}, b[1,0]: {}".format(b[0,0], b[0,1], b[1,0]))

    def example2(self):
        a = np.zeros((2,2))                     # Create an array of all zeros
        print("np.zeroes(2,2)\n", a)              # Prints "[[ 0.  0.]
                                                #          [ 0.  0.]]"

        b = np.ones((1,2))                      # Create an array of all ones
        print("np.ones(1,2)\n", b)                # Prints "[[ 1.  1.]]"

        c = np.full((2,2), 7)                   # Create a constant array
        print("np.full((2,2), 7)\n", c)           # Prints "[[ 7.  7.]
                                                #          [ 7.  7.]]"

        d = np.eye(2)                           # Create a 2x2 identity matrix
        print("np.eye(2)\n", d)                   # Prints "[[ 1.  0.]
                                                #          [ 0.  1.]]"

        e = np.random.random((2,2))             # Create an array filled with random values
        print("np.random.random((2,2))\n", e)     # Might print "[[ 0.91940167  0.08143941]
                                                #               [ 0.68744134  0.87236687]]"

    def example3(self):
        # Create the following rank 2 array with shape (3, 4)
        # [[ 1  2  3  4]
        #  [ 5  6  7  8]
        #  [ 9 10 11 12]]
        a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
        
        # Use slicing to pull out the subarray consisting of the first 2 rows
        # and columns 1 and 2; b is the following array of shape (2, 2):
        # [[2 3]
        #  [6 7]]
        b = a[:2, 1:3]
        print("b\n", b)

        # A slice of an array is a view into the same data, so modifying it
        # will modify the original array.
        print("a[0,1]\n", a[0,1])
        b[0,0] = 77                             # b[0, 0] is the same piece of data as a[0, 1]
        print("a[0,1]\n", a[0,1])

    def example4(self):
        # Create the following rank 2 array with shape (3, 4)
        # [[ 1  2  3  4]
        #  [ 5  6  7  8]
        #  [ 9 10 11 12]]
        a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

        # Two ways of accessing the data in the middle row of the array.
        # Mixing integer indexing with slices yields an array of lower rank,
        # while using only slices yields an array of the same rank as the
        # original array:
        row_r1 = a[1, :]    # Rank 1 view of the second row of a  
        row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
        print("row_r1:", row_r1, "row_r1.shape:",  row_r1.shape)  # Prints "[5 6 7 8] (4,)"
        print ("row_r2:", row_r2, "row_r2.shape:", row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

        # We can make the same distinction when accessing columns of an array:
        col_r1 = a[:, 1]
        col_r2 = a[:, 1:2]
        print("col_r1:", col_r1, "col_r1.shape:", col_r1.shape)  # Prints "[ 2  6 10] (3,)"
        print("col_r2:", col_r2, "col_r2.shape:", col_r2.shape)  # Prints "[[ 2]
                                                                 #          [ 6]
                                                                 #          [10]] (3, 1)     "



if __name__ == "__main__":
    npe = NumPyExample()
    print("example1:")
    npe.example1()
    print("example2:")
    npe.example2()
    print("example3:")
    npe.example3()
    print("example4:")
    npe.example4()



