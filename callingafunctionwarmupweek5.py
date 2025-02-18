#Adding Sequence to each number in a list

"""
    Adds 1, then 2, then 3, and so on to each number in the list.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    list: A new list with the sequence added to each number.
    """
def add_sequence(lst):
    return [num + i for i, num in enumerate(lst, start=1)]


nums1 = [10, 20, 30, 40]
print("List before function: " + str(nums1))
print("List After calling function: " + str(add_sequence(nums1)))  # Output: [11, 22, 33, 44]

print()

nums2 = [100,200,300,400,500,600,700,800,900]
print("List before funcation: " + str(nums2))
print("List After calling function: " + str(add_sequence(nums2)))  # Output: [101, 202, 303, 404, 505, 606, 707, 808, 909]

