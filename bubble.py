def bubble_sort(arr):
    n=len(arr) #get the lenth of array
    for i in range(n): #n loop#outer loop
        for j in range(0, n-i-1):#iner loop
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage:
arr = [16, 34,14 , 12, 22, 45, 98]
sorted_arr = bubble_sort(arr)
print("Sorted array is:", sorted_arr)
