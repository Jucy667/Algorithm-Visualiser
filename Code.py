import matplotlib.pyplot as plt
import numpy as np

# Get the number of elements to sort
n = int(input("Enter the number of elements you want to sort: "))

#Get the speed level of the animation
spd = float(input("How fast would you like the animation to be? (1. fast, 2. medium, 3. slow): "))
speed = int()

# Set the speed based on user input
if spd == 1:
    speed = 0.05
elif spd == 2:
    speed = 0.2
elif spd == 3:
    speed = 0.5

# Generate an array integers from 1 to n then shuffle them
array = np.random.permutation(np.arange(1, n+1))

# represents the x-axis aka. the index of each element
x = np.arange(0, n, 1)

# prints the original array
print(array)

# Bubble Sort visualiser
length = len(array)

for i in range(length):
    for j in range(length - i - 1):
        plt.title("Bubble Sort Visualisation")
        plt.bar(x, array, color='grey')
        plt.xlabel("Index of item in list")
        plt.ylabel("Value")
        plt.pause(speed)
        plt.clf()

        #bubble sort algorithm
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            
# Plot the final sorted array so the chart stays visible
plt.title("Bubble Sort Visualisation")
plt.bar(x, array, color='grey')
plt.xlabel("Index of item in list")
plt.ylabel("Value")
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