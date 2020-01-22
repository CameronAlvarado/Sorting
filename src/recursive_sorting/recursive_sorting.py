# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [None] * elements
    # TO-DO
    # indexes
    a = 0
    b = 0
    for i in range(elements):
        if a >= len(arrA): # if there are no more elements in left side 
            merged_arr[i] = arrB[b] # merge from the right side
            b +=1 #increment index for right side
        elif b >= len(arrB): #if no elements in right side
            merged_arr[i] = arrA[a] #merge from the left side
            a += 1 #increment index for left side
        elif arrA[a] < arrB[b]: #check first element of each list to see which one is greater
            merged_arr[i] = arrA[a]
            a += 1
        else: 
            merged_arr[i] = arrB[b]
            b += 1
    print('\n Merged list',merged_arr)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    # if length of list is greater than 1,
    # split list in half

    # if length of list is equal to one, 
    # list is sorted
    if len(arr) <= 1:
        return arr
    else:
        LHA = merge_sort(arr[:len(arr) // 2])
        RHA = merge_sort(arr[len(arr) // 2:])
        # merge smaller lists together into bigger lists
        return merge(LHA, RHA)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr



# quick sort sudo:

# select first index as a pivot
# move all elements smaller than pivot to an array to the left
# move elements greater than pivot to an array to the right
# while <- left arr and right arr are greater than 1,
# repeat last three steps on each arr (left and right)