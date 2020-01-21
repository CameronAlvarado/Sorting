def swap_positions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)): # used to be len(arr) - 1
        # print(arr)
        cur_index = i
        cur_minimuim = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 l.o.c.
        for j in range(cur_minimuim, cur_index):
            if j < arr[0]:
                cur_minimuim = j

        # TO-DO: swap
        arr[cur_minimuim] = cur_index


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    arr_length = len(arr)
    for i in range(0, arr_length):
        # print(arr)
        cur_index = i
        cur_minimuim = cur_index
        for j in range(cur_minimuim, cur_index):
            if j < j + 1:
                cur_minimuim = j

        # TO-DO: swap
        arr[cur_index] = cur_minimuim

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr