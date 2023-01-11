# Name: Jacob Summers
# Date: 10.8.22
# Course: CS 325 Section: 400
# Assignment: 2 problem 3b
# Description: Algorithm uses variation of the merge sort with divide and conquer to return the index of which element
#               would be found in a merged array at a specific 'kth' place in a new merged array.

def kthElement(arr1, arr2, k):
    """Function takes 2 sorted arrays and an index as parameters and creates a single merged array with
    elements from both parameter passed arrays in order. The function then uses the passed index to return
    which element would be found at the 'kth' position in the merged array."""
    index_1 = 0
    index_2 = 0
    k_element = None
    merge_index = 0
    arr1_element = arr1[index_1]
    arr2_element = arr2[index_2]

    while index_1 < len(arr1) and index_2 < len(arr2) and merge_index < k:
        arr1_element = arr1[index_1]
        arr2_element = arr2[index_2]
        if arr1_element < arr2_element:
            k_element = arr1_element
            merge_index += 1
            index_1 += 1
        else:
            k_element = arr2[index_2]
            index_2 += 1
            merge_index += 1
    while index_1 < len(arr1) and merge_index < k:
        k_element = arr1[index_1]
        merge_index += 1
        index_1 += 1

    while index_2 < len(arr2) and merge_index < k:
        k_element = arr2[index_2]
        merge_index += 1
        index_2 += 1
    return k_element


#arr1 = [1,2,3,5,6]
#arr2 = [3,4,5,6,7]
#print(kthElement(arr1, arr2, 5))