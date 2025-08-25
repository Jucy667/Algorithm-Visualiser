# Dependencies

import matplotlib.pyplot as plt
import numpy as np

# Initialising the counter variables

bubble_comparisons = 0
bubble_swaps = 0
selection_comparisons = 0
selection_swaps = 0
insertion_comparisons = 0
insertion_swaps = 0

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
array = np.random.randint(1, 100, size=n)

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
plt.title(f"Selection Sort Visualisation\nComparisons: {selection_comparisons}  Swaps: {selection_swaps}")
plt.bar(x, arr2, color='orange')
plt.xlabel("Index of item in list")
plt.ylabel("Value")
plt.figtext(0.5, 0.02, "Selection Sort Time Complexity: O(n^2)", ha="center", fontsize=10, color='orange')

plt.subplot(1,3,3)
plt.title(f"Insertion Sort Visualisation\nComparisons: {insertion_comparisons}  Swaps: {insertion_swaps}")
plt.bar(x, arr3, color='limegreen')
plt.xlabel("Index of item in list")
plt.ylabel("Value")
plt.figtext(0.83, 0.02, "Insertion Sort Time Complexity: O(n^2)", ha="center", fontsize=10, color='limegreen')
plt.pause(0.001)  # Short pause to render

# Bubble Sort visualiser

for i in range(length):
    for j in range(0,length - i - 1):
        bubble_comparisons += 1  # Increment the counter for each comparison
        plt.subplot(1,3,1)
        plt.title(f"Bubble Sort Visualisation\nComparisons: {bubble_comparisons}  Swaps: {bubble_swaps}")
        plt.bar(x, arr1, color='dodgerblue')
        plt.xlabel("Index of item in list")
        plt.ylabel("Value")
        plt.figtext(0.17, 0.02, "Bubble Sort Time Complexity: O(n^2)", ha="center", fontsize=10, color='dodgerblue')
        plt.pause(speed)
        plt.cla()
        # Bubble sort algorithm
        if arr1[j] > arr1[j + 1]:
            arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
            bubble_swaps += 1

# Plot the final sorted Bubble Sort visualisation so the chart stays visible
plt.subplot(1,3,1)
plt.title(f"Bubble Sort Visualisation\nComparisons: {bubble_comparisons}  Swaps: {bubble_swaps}")
plt.bar(x, arr1, color='green')
plt.xlabel("Index of item in list")
plt.ylabel("Value")
plt.pause(0.001)  # Short pause to render
plt.figtext(0.17, 0.02, "Bubble Sort Time Complexity: O(n^2)", ha="center", fontsize=10, color='dodgerblue')

# Selection Sort Visualiser

for i in range(length):
    cur_min_idx = i
    for j in range(i+1, length):
        selection_comparisons += 1  # Increment the counter for each comparison
        plt.subplot(1,3,2)
        plt.title(f"Selection Sort Visualisation\nComparisons: {selection_comparisons}  Swaps: {selection_swaps}")
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
    if cur_min_idx != i:
        arr2[i], arr2[cur_min_idx] = arr2[cur_min_idx], arr2[i]
        selection_swaps += 1

plt.subplot(1,3,2)
plt.title(f"Selection Sort Visualisation\nComparisons: {selection_comparisons}  Swaps: {selection_swaps}")
plt.bar(x, arr2, color='green')
plt.xlabel("Index of item in list")
plt.ylabel("Value")
plt.pause(0.001)  # Short pause to render
plt.figtext(0.5, 0.02, "Selection Sort Time Complexity: O(n^2)", ha="center", fontsize=10, color='orange')

# Insertion Sort visualiser

for i in range(1, length):
    j = i
    plt.subplot(1,3,3)
    plt.title(f"Insertion Sort Visualisation\nComparisons: {insertion_comparisons}  Swaps: {insertion_swaps}")
    plt.bar(x, arr3, color='limegreen')
    plt.xlabel("Index of item in list")
    plt.ylabel("Value")
    plt.pause(speed)
    plt.cla()
    while j > 0:
        insertion_comparisons += 1  # Increment the counter for each comparison
        
        # Insertion sort algorithm
        if arr3[j] < arr3[j-1]:
            arr3[j], arr3[j-1] = arr3[j-1], arr3[j]
            j -= 1
            insertion_swaps += 1
        else:
            break
    

plt.subplot(1,3,3)
plt.title(f"Insertion Sort Visualisation\nComparisons: {insertion_comparisons}  Swaps: {insertion_swaps}")
plt.bar(x, arr3, color='green')
plt.xlabel("Index of item in list")
plt.ylabel("Value")
plt.figtext(0.83, 0.02, "Insertion Sort Time Complexity: O(n^2)", ha="center", fontsize=10, color='limegreen')
plt.show()