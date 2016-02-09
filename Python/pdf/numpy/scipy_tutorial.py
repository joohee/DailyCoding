from scipy.misc import imread, imsave, imresize
import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt

class ScipyTutorial():
    def __init__(self):
        pass

    def image_operation(self):
        img = imread("assets/cat.jpg")
        print("img.dtype, img.shape", img.dtype, img.shape)

        # image scaling
        img_tinted = img * [1, 0.95, 0.9]       # rgb

        # img resize
        img_tinted = imresize(img_tinted, (300, 300))

        imsave("assets/cat_tinted.jpg", img_tinted)
        print("image saved to cat_tinted")

    def distance(self):
        x = np.array([[0,1], [1,0], [2,0]])
        print("x\n", x)

        # 모든 요소들에 대해 Euclidean distance 를 구한다. 
        # d[i, j] is the Euclidean distance between x[i, :] and x[j, :],
        # and d is the following array:
        # [[ 0.          1.41421356  2.23606798]
        #  [ 1.41421356  0.          1.        ]
        #  [ 2.23606798  1.          0.        ]]
        d = squareform(pdist(x, 'euclidean'))
        print("d\n", d)

    def matplotlib_plotting(self):
        # sin함수를 이용해 x, y커브를 구한다.
        x = np.arange(0, 3 * np.pi, 0.1)
        y = np.sin(x)

        # matplotlib를 이용해서 점을 나타낸다. (plot the points)
        plt.plot(x, y)
        # 실행해보면 그래프가 보이지 않는다. 왜지?
        plt.show()

    def matplotlib_plotting_multiple_lines(self):
        x = np.arange(0, 3 * np.pi, 0.1)
        y_sin = np.sin(x)
        y_cos = np.cos(x)

        plt.plot(x, y_sin)
        plt.plot(x, y_cos)
        plt.xlabel('x axis label')
        plt.ylabel('y axis label')
        plt.title('Sine and Cosine')
        plt.legend(['Sine', 'Cosine'])
        plt.show()


if __name__ == "__main__":
    tutorial = ScipyTutorial()

    #print("image operation\n")
    #tutorial.image_operation()
    #print("distance among all rows of matrix\n")
    #tutorial.distance()
    #print("plot the points\n")
    #tutorial.matplotlib_plotting();
    print("plot the points with multiple lines.\n")
    tutorial.matplotlib_plotting_multiple_lines()








