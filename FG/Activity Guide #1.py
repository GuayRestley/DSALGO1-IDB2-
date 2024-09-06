#1.[23,89, 7, 56, 44]
arr3 = [23, 89, 7, 56, 44]
print("#1 before bubble sort:")
print(arr3)

def BubbleSort(arr3):
    for i in range(len(arr3)):
        for j in range(0, len(arr3) - i - 1):
            if arr3[j] > arr3[j + 1]:
                arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]

BubbleSort(arr3)
print("#1 after bubble sort:")
print(arr3)


#2.[12, 78, 91, 34, 62]
arr1 = [12, 78, 91, 34, 62]
print("#2 before insertion sort:")
print(arr1)

def InsertionSort(arr1):
    for i in range(1, len(arr1)):
        key = arr1[i]
        j = i - 1
        # Move elements of arr1[0..i-1]
        # that are greater than the key
        # to one position ahead of their current position
        while j >= 0 and key < arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key

InsertionSort(arr1)
print("#2 after insertion sort:")
print(arr1)


#3. [5, 99, 48, 15, 67]
arr2 = [5, 99, 48, 15, 67]
print("#3 before selection sort:")
print(arr2)

def SelectionSort(arr2):
    for i in range(len(arr2)):
        min_inx = i
        for j in range(i + 1, len(arr2)):
            if arr2[min_inx] < arr2[j]:
                min_inx = j
        # Swapping the values from our array
        arr2[i], arr2[min_inx] = arr2[min_inx], arr2[i]

SelectionSort(arr2)
print("#3 after selection sort:")
print(arr2)

#4. [38, 82, 25, 74, 13]
arr1 = [38, 82, 25, 74, 13]
print("#4 before insertion sort:")
print(arr1)

def InsertionSort(arr1):
    for i in range(1, len(arr1)):
        key = arr1[i]
        j = i - 1
        # Move elements of arr1[0..i-1]
        # that are greater than the key
        # to one position ahead of their current position
        while j >= 0 and key > arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key

InsertionSort(arr1)
print("#4 after insertion sort:")
print(arr1)


#5.
# Copying values from the second index and third index of previous datasets
dataset = [
    arr3[2],  # Value from arr3
    arr3[3],  # Value from arr3
    arr1[2],  # Value from arr1
    arr1[3],  # Value from arr1
    arr2[2],  # Value from arr2
    arr2[3],  # Value from arr2
    arr1[2],  # Value from arr4
    arr1[3]   # Value from arr4
]

print("Dataset with copied values:")
print(dataset)

# Sorting in ascending order
def SelectionSort(dataset):
    for i in range(len(dataset)):
        min_inx = i
        for j in range(i + 1, len(dataset)):
            if dataset[min_inx] > dataset[j]:
                min_inx = j
        # Swapping the values from our array
        dataset[i], dataset[min_inx] = dataset[min_inx], dataset[i]

SelectionSort(dataset)
print("#5 Ascending Order")
print(dataset)


# Sorting in descending order
def SelectionSort(dataset):
    for i in range(len(dataset)):
        min_inx = i
        for j in range(i + 1, len(dataset)):
            if dataset[min_inx] < dataset[j]:
                min_inx = j
        # Swapping the values from our array
        dataset[i], dataset[min_inx] = dataset[min_inx], dataset[i]

SelectionSort(dataset)
print("#5 Descending Order")
print(dataset)


#6.
# Combine all values from the arrays used in 1 to 4
combined_list = arr3 + arr1 + arr2 + arr1
print("Combined list before selection sort:")
print(combined_list)

def SelectionSort(arr):
    for i in range(len(arr)):
        min_inx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_inx]:
                min_inx = j
        arr[i], arr[min_inx] = arr[min_inx], arr[i]

# Apply Selection Sort
SelectionSort(combined_list)
print("Combined list after selection sort (ascending):")
print(combined_list)




#7.
# Even and odd values from the sorted list in item 6
even_values = [x for x in combined_list if x % 2 == 0]
odd_values = [x for x in combined_list if x % 2 != 0]

print("Even values:")
print(even_values)

print("Odd values:")
print(odd_values)
