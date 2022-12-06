# import json
# import os

# # Take note of the directory you are running this from to properly open the json
# f = open("Code/Projects/Project 3/video_games.json")
# data = json.load(f)

# This function is derived from Naresh's code for shell sort
# The function takes in two dictionaries from the json, and will return true
# if leftGame is more relevant to the search parameters than rightGame
def compareRelevance(leftGame, rightGame, genres, priceRange, timeRange, online):
    leftrelevance, rightrelevance = 0, 0
    averageprice = (priceRange[0] + priceRange[1]) // 2
    averagetime = (timeRange[0] + timeRange[1]) // 2

    if abs(rightGame["Metrics"]["Used Price"] - averageprice) < abs(leftGame["Metrics"]["Used Price"] - averageprice):
        rightrelevance += 1
    else:
        leftrelevance += 1
    if abs(rightGame["Length"]["All PlayStyles"]["Average"] - averagetime) < abs(leftGame["Length"]["All PlayStyles"]["Average"] - averagetime):
        rightrelevance += 1
    else:
        leftrelevance += 1
    if rightGame["Metadata"]["Genres"] in genres:
        rightrelevance += 1
    if leftGame["Metadata"]["Genres"] in genres:
        leftrelevance += 1
    if online != 2:
        if online == 1:
            if leftGame["Features"]["Online?"] == True:
                leftrelevance += 1
            if rightGame["Features"]["Online?"] == True:
                rightrelevance += 1
        else:
            if leftGame["Features"]["Online"] == False:
                leftrelevance += 1
            if rightGame["Features"]["Online"] == False:
                rightrelevance += 1
    return leftrelevance > rightrelevance


# This function determines the minimum size of a run;
# to explain the importance of this I have to explain Timsort.
# Timsort takes advantage of the fact that naturally ocurring data
# often has sections that are alredy sorted within themselves.
# So instead of naively merging all the way, Timsort starts by
# merging already sorted portions, or runs.
# Timsort is optimized when len(arr)/minRun == 2^k (or slightly less)
# and 32 <= minrun <= 64
# The calcMinRun function calculates a minRun value 
# to satisfy these condition, taking advantage of bit manipulations
# that work nicely with powers of 2.
# Note the original explanation for this function in python docs:
# "take the first 6 bits of N, and add 1 if any of the remaining bits are set"
def calcMinRun(n):
    initial = n
    r = 0
    while n >= 32:
        r |= n & 1 # calculates the remainder (if number is odd (n&1), r = 1)
        n >>= 1 # divide n by 2 (floor)
    return n + r
 
 
# This function sorts array from indices 
# l through r, where r-l <= RUN
# The other core concept of Timsort I haven't explained
# is the use of insertion sort.
# Naturally ocurring runs are all types of sizes;
# To bring them up to length minRun, insertion sort is used
# since the naturally sorted part can be the initial sorted portion
def insertionSort(arr, left, right, genres, priceRange, timeRange, online):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and compareRelevance(arr[j], arr[j - 1], genres, priceRange, timeRange, online):
            # move the next element back through the sorted
            # portion until in the right place
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
 
# Merging the sorted runs
def merge(arr, l, m, r, genres, priceRange, timeRange, online):
 
    # original array is broken in two parts
    # left and right array
    len0 = m - l + 1
    len1 = r - m
    left, right = [], []
    for i in range(0, len0): left.append(arr[l + i])
    for i in range(0, len1): right.append(arr[m + 1 + i])
 
    i, j = 0, 0
    k = l
 
    # merge subarrays
    while i < len0 and j < len1:
        if compareRelevance(left[i], right[j], genres, priceRange, timeRange, online):
            arr[k] = left[i]
            i += 1
 
        else:
            arr[k] = right[j]
            j += 1
 
        k += 1
 
    # Copy any remaining elements of left
    while i < len0:
        arr[k] = left[i]
        k += 1
        i += 1
 
    # Copy any remaining element of right
    while j < len1:
        arr[k] = right[j]
        k += 1
        j += 1
 
 
# implements the previous two functions in timSort
def tim_sort(arr, genres, priceRange, timeRange, online, ):
    n = len(arr)
    minRun = calcMinRun(n)
 
    # Sort subarrays of size RUN
    for start in range(0, n, minRun):
        # Note how the next line Accounts for the array possibly being <64 elements,
        # in which case RUN = n. Since there aren't multiple runs to merge, this
        # means that Timsort will reduce to just the insertion sort part
        # in the actual implementation of Timsort, a binary insertion sort would 
        # be used, but considering the size of the video games data set, this will
        # not usuallly be the case.
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end, genres, priceRange, timeRange, online)
 
    # Start merging from size RUN. It will merge
    # to form size 64, then 128, etc until whole array sorted
    # The idea is that this is basically a merge sort,
    # but instead of going down to a singular element and recursively merging,
    # Timsort starts by merging pairs of equally sized runs.
    size = minRun
    while size < n:
 
        # Iterate through the array 2 runs at a time
        for left in range(0, n, 2 * size):
 
            # Find the mid and right values with the knowledge that
            # size is the size of currently sorted subarrays
            # we need to consider that we could hit end of array, hence the min with n-1
            mid = min(left + size - 1, n-1)
            right = min((left + 2 * size - 1), n - 1)
 
            #Merge the subarrays
            if mid < right:
                merge(arr, left, mid, right, genres, priceRange, timeRange, online)
 
        size = 2 * size
    return arr[:15]

# if __name__ == "__main__":
#     tim_sort(data, ["Simulation"], (20, 40), (0, 10), 1)
#     for i in range(15): print(data[i]['Title'])
    