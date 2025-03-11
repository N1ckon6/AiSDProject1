import sys
import random 

def insertion_sort(data):
    for j in range(len(data) - 1):
        for i in range(len(data) - j - 1):
            if(data[i] > data[i+1]):
                data[i], data[i+1] = data[i+1], data[i]

def shell_sort(data):
    k = len(data) // 2
    while(k > 0):
        for i in range(k):
            temporary_list = []
            element_number = 0
            for j in range(i, len(data), k):
                temporary_list.append(data[j])
            insertion_sort(temporary_list)
            for n in range(i, len(data), k):
                data[n] = temporary_list[element_number]
                element_number += 1
        k = k // 2

def selection_sort(data):
    for j in range(len(data) - 1):
        min = j
        for i in range(j + 1, len(data)):
            if data[i] < data[min]:
                min = i
        data[j], data[min] = data[min], data[j]

def heap_sort(data):
    def heapify(data, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[i] < data[left]:
            largest = left

        if right < n and data[largest] < data[right]:
            largest = right

        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            heapify(data, n, largest)

    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

def quick_sort_left_pivot(data):
    def partition(data, low, high): 
        i = high + 1 
        pivot = data[low] 
 
        for j in range(high, low, -1): 
            if data[j] > pivot: 
                i -= 1 
                data[i], data[j] = data[j], data[i] 
 
        data[i - 1], data[low] = data[low], data[i - 1] 
        return i - 1 
 
    def quick_sort_rec(data, low, high): 
        if low < high: 
            pi = partition(data, low, high) 
            quick_sort_rec(data, low, pi - 1) 
            quick_sort_rec(data, pi + 1, high) 
             
             
 
    quick_sort_rec(data, 0, len(data) - 1) 
 
def quick_sort_random_pivot(data):
    def partition(data, low, high): 
        i = high + 1 
        pivot_index = random.randint(low, high) 
        data[low], data[pivot_index] = data[pivot_index], data[low] 
        pivot = data[low] 
 
        for j in range(high, low, -1): 
            if data[j] > pivot: 
                i -= 1 
                data[i], data[j] = data[j], data[i] 
 
        data[i - 1], data[low] = data[low], data[i - 1] 
        return i - 1 
 
    def quick_sort_rec(data, low, high): 
        if low < high: 
            pi = partition(data, low, high) 
            quick_sort_rec(data, low, pi - 1) 
            quick_sort_rec(data, pi + 1, high) 
             
             
 
    quick_sort_rec(data, 0, len(data) - 1)

def sort_using_algorithm(data, algorithm):
    # This function takes the algorithm identifier as input
    # However, it always uses the sorted function in Python

    if algorithm == 1:
        insertion_sort(data)
    elif algorithm == 2:
        shell_sort(data)
    elif algorithm == 3:
        selection_sort(data)
    elif algorithm == 4:
        heap_sort(data)
    elif algorithm == 5:
        quick_sort_left_pivot(data)
    elif algorithm == 6:
        quick_sort_random_pivot(data)

    return data

def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input=sys.stdin.read().split()
    try:
        data = [int(x) for x in input]
    except EOFError:
        print("Error reading input.")

    # Perform sorting using the specified algorithm (ignored in this example)
    sorted_data = sort_using_algorithm(data, algorithm_number)

    # Print the sorted data
    print("Sorted data:", sorted_data[0:10])

if __name__ == "__main__":
    main()