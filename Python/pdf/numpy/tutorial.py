import numpy as np

class NumPyExample():
    def __init__(self):
        pass

    # Initialize numpy arrays from nested Python lists and access elements using square bracket. 
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

    # Many functions to create array
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

    # Array indexing - slicing.
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

    # Mix integer indexing with slice indexing. 
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

    # Integer array indexing 
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

    # one useful trick with integer array indexing is selecting or mutating one element from each row of a matrix
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
    # Boolean array indexing
    def example7(self):
        a = np.array([[1,2],[3,4],[5,6]])
        bool_index = (a > 2)
        print("bool_index\n", bool_index)

        print("a[bool_index]\n", a[bool_index])
        print("a[a > 2]\n", a[a > 2])


    # Datatypes - numpy try to guess the datatype of array, and you can force to explicitly specify the datatype. 
    def example8(self):
        x = np.array([1,2])
        print("x.dtype\n", x.dtype)

        x = np.array([1.0, 2.0])
        print("x.dtype\n", x.dtype)

        x = np.array([1,2], dtype=np.int32)
        print("x.dtype\n", x.dtype)

    # Array math  * (multiply)는 각 요소의 곱의 합이 아니라 matrix 곱셈이다. 
    # 곱의 합을 나타내고 싶으면 . (dot)을 이용해야 한다. 
    def example9(self):
        x = np.array([[1,2], [3,4]], dtype=np.float64)
        y = np.array([[5,6], [7,8]], dtype=np.float64)

        print("x+y\n", x+y)
        print("np.add(x,y)\n", np.add(x,y))

        print("x-y\n", x-y)
        print("np.subtract(x,y)\n", np.subtract(x,y))

        print("x*y\n", x*y)
        print("np.multiply(x,y)\n", np.multiply(x,y))

        print("x/y\n", x/y)
        print("np.divide(x,y)\n", np.divide(x,y))

    # .(dot) function - You can get the product of multiply.
    def example10(self):
        x = np.array([[1,2],[3,4]])
        y = np.array([[5,6],[7,8]])

        v = np.array([9,10])
        w = np.array([11,12])

        # .(dot)을 이용하면 합을 얻을 수 있다. 
        print("v.dot(w)\n", v.dot(w))
        print("np.dot(v,w)\n", np.dot(v,w))

        # matrix 끼리의 곱셈 연산 결과도 얻을수 있다. 
        # 결과는 둘다 1 차 rank (차원?행렬) [ 29 67 ]이 된다. 
        print("x.dot(v)\n", x.dot(v))
        print("np.dot(x,v)\n", np.dot(x,v))

        # 결과는 둘다 2 차 rank (차원?행렬)이 된다. 
        #  [[19 22]
        #   [ 43 50]]
        print("x.dot(y)\n", x.dot(y))
        print("np.dot(x,y)\n", np.dot(x,y))

    # the useful functions of numpy - sum
    def example11(self):
        x = np.array([[1,2],[3,4]])
        print("np.sum(x)\n", np.sum(x))         # compute sum of all elements
        print("np.sum(x, axis=0)\n", np.sum(x, axis=0))         # compute sum of each column - [4 6]
        print("np.sum(x, axis=1)\n", np.sum(x, axis=1))         # compute sum of each row - [3 7]

    # You can transport a matrix using T
    def example12(self):
        x = np.array([[1,2],[3,4]])
        print("x\n", x)
        print("x.T\n", x.T)

        # 하지만 1차원 배열에서 T는 변화가 없다. 
        v = np.array([1,2,3])
        print("v\n", v)
        print("v.T\n", v.T)

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
    print("\nexample7:")
    npe.example7()
    print("\nexample8:")
    npe.example8()
    print("\nexample9:")
    npe.example9()
    print("\nexample10:")
    npe.example10()
    print("\nexample11:")
    npe.example11()
    print("\nexample12:")
    npe.example12()



