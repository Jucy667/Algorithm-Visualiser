# Dependencies

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

# Create three copies of the array for each sorting algorithm
arr1 = array.copy()
arr2 = array.copy()
arr3 = array.copy()

# Represents the x-axis aka. the index of each element
x = np.arange(0, n, 1)

# Prints the original array for the user to see
print(array)


# Just qol stuff.
length = len(array)

# Plot initial Selection and Insertion Sort graph (unsorted)
plt.subplot(1,3,2)
plt.title("Selection Sort Visualisation")
plt.bar(x, arr2, color='orange')
plt.xlabel("Index of item in list")
plt.ylabel("Value")

plt.subplot(1,3,3)
plt.title("Insertion Sort Visualisation")
plt.bar(x, arr3, color='limegreen')
plt.xlabel("Index of item in list")
plt.ylabel("Value")
plt.pause(0.001)  # Short pause to render

# Bubble Sort visualiser
for i in range(length):
    for j in range(length - i - 1):
        plt.subplot(1,3,1)
        plt.title("Bubble Sort Visualisation")
        plt.bar(x, arr1, color='dodgerblue')
        plt.xlabel("Index of item in list")
        plt.ylabel("Value")
        plt.pause(speed)
        plt.cla()
        # Bubble sort algorithm
        if arr1[j] > arr1[j + 1]:
            arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]

# Plot the final sorted Bubble Sort visualisation so the chart stays visible
plt.subplot(1,3,1)
plt.title("Bubble Sort Visualisation")
plt.bar(x, arr1, color='green')
plt.xlabel("Index of item in list")
plt.ylabel("Value")
plt.pause(0.001)  # Short pause to render

# Selection Sort Visualiser
for i in range(length):
    cur_min_idx = i
    for j in range(i+1, length):
        plt.subplot(1,3,2)
        plt.title("Selection Sort Visualisation")
        plt.bar(x, arr2, color='orange')
        plt.xlabel("Index of item in list")
        plt.ylabel("Value")
        plt.pause(speed)
        plt.cla()

        # Selection sort algorithm
        if arr2[j] < arr2[cur_min_idx]:
            cur_min_idx = j
        else:
            cur_min_idx = cur_min_idx
    arr2[i], arr2[cur_min_idx] = arr2[cur_min_idx], arr2[i]

plt.subplot(1,3,2)
plt.title("Selection Sort Visualisation")
plt.bar(x, arr2, color='green')
plt.xlabel("Index of item in list")
plt.ylabel("Value")
plt.pause(0.001)  # Short pause to render


# Insertion Sort visualiser


for i in range(length):
    for j in range(i+1, length):
        plt.subplot(1,3,3)
        plt.title("Insertion Sort Visualisation")
        plt.bar(x, arr3, color='limegreen')
        plt.xlabel("Index of item in list")
        plt.ylabel("Value")
        plt.pause(speed)
        plt.cla()
        
        # Insertion sort algorithm
        while arr3[j] < arr3[j-1] and j > 0:
            arr3[j], arr3[j-1] = arr3[j-1], arr3[j]
            j -= 1
            
plt.subplot(1,3,3)
plt.title("Insertion Sort Visualisation")
plt.bar(x, arr3, color='green')
plt.xlabel("Index of item in list")
plt.ylabel("Value")
plt.show()