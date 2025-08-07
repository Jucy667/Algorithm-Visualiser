import matplotlib.pyplot as plt
import numpy as np

n = int(input("Enter the number of elements you want to sort: "))

array = np.random.permutation(np.arange(1, n+1))
x = np.arange(0, n, 1)
print(array)


length = len(array)

for i in range(length):
    for j in range(length - i - 1):
        plt.title("Bubble Sort Visualisation")
        plt.bar(x, array, color='grey')
        plt.pause(0.1)
        plt.clf()
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
plt.show()



#PSUEDO CODE FOR SELECTION SORT

# in array check the first element
# set the first element as a variable minimum
# check next element compare with minimum
# repeat until end of array
# set first array to temp
# set minimum to first element
# set temp to where minimum was
# check next element and repeat.
# iteration stops at last element