# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    arr = arrA + arrB
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 lines of code) 
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TODO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]


    return arr


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