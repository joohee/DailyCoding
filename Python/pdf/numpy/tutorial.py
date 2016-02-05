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
        row_r1 = a[1, :]    # Rank 1 view of the second row of a, 1차원 배열만 리턴. 
        row_r2 = a[1:2, :]  # Rank 2 view of the second row of a, 1:2에서 2번째는 포함되지 않으므로 이중 배열로 리턴. 데이터는 위와 동일. 
        print("row_r1:", row_r1, "row_r1.shape:",  row_r1.shape)  # Prints "[5 6 7 8] (4,)"
        print ("row_r2:", row_r2, "row_r2.shape:", row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

        # We can make the same distinction when accessing columns of an array:
        col_r1 = a[:, 1]
        col_r2 = a[:, 1:2]
        print("col_r1:", col_r1, "col_r1.shape:", col_r1.shape)  # Prints "[ 2  6 10] (3,)"
        print("col_r2:", col_r2, "col_r2.shape:", col_r2.shape)  # Prints "[[ 2]
                                                                 #          [ 6]
                                                                 #          [10]] (3, 1)     "

    def example5(self):
        a = np.array([[1,2], [3,4], [5,6]])
        # An example of integer array indexing.
        # The returned array will have shape (3,) and 
        print ("a[[0,1,2],[0,1,0]]):\n", a[[0,1,2], [0,1,0]])        # Prints "[1 4 5]". 2*3 배열의 [0,0], [1,1], [2,0] 값이므로 [1,4,5]가 된다. 

        # When using integer array indexing, you can reuse the same
        # element from the source array:
        print("a[[0, 0], [1, 1]]:", a[[0, 0], [1, 1]])  # Prints "[2 2]"

        # Equivalent to the previous integer array indexing example
        print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"

    def example6(self):
        # create a new array from which we will select elements
        a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

        print("a\n", a)          # prints "array([[ 1,  2,  3],
                                 #                [ 4,  5,  6],
                                 #                [ 7,  8,  9],
                                 #                [10, 11, 12]])"

        # create a array of indices
        b = np.array([0,2,0,1])
        
        # select one element from each row of a using the indices in b
        print("a[np.arange(4), b])\n", a[np.arange(4), b])      # prints "[ 1 6 7 11 ]

        # mutate one element from each row of a using hte indices in b
        a[np.arange(4), b] += 10

        print("a\n", a)             # prints "array([[11,  2,  3],
                                    #                [ 4,  5, 16],
                                    #                [17,  8,  9],
                                    #                [10, 21, 12]])
        



if __name__ == "__main__":
    npe = NumPyExample()
    print("\nexample1:")
    npe.example1()
    print("\nexample2:")
    npe.example2()
    print("\nexample3:")
    npe.example3()
    print("\nexample4:")
    npe.example4()
    print("\nexample5:")
    npe.example5()
    print("\nexample6:")
    npe.example6()




