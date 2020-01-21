# def swap_positions(list, pos1, pos2): 
      
#     list[pos1], list[pos2] = list[pos2], list[pos1] 
#     return list

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(0, len(arr)): # used to be len(arr) - 1
        print(arr)
        min_index = i
        for j in range(min_index, i):
            if j < arr[0]:
                min_index = j

        arr[min_index] = i

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    arr_length = len(arr)
    for i in range(0, arr_length):
        cur_minimuim = i
        for j in range(cur_minimuim, i):
            if j < j + 1:
                cur_minimuim = j

        arr[i] = cur_minimuim

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr