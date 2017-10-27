
# def first_non_consecutive(arr):
#     for i, n in enumerate(arr):
#         if i <= len(arr) - 2 and arr[i+1] - arr[i] != 1:
#             return arr[i+1]
#     return None

# def first_non_consecutive(arr):
#     return next((j for i, j in zip(arr, arr[1:]) if i + 1 != j), None)
#
def first_non_consecutive(arr):
    for i, j in zip([1,2,3,4,6,7,8], [2,3,4,6,7,8]):
        if abs(j-i) > 1:
            return j
    return None

print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))