# D. remove_adjacent
def remove_adjacent(nums):
    if not nums:
        return []
    
    result = [nums[0]]  # Start with the first element
    for num in nums[1:]:  # Loop through the rest of the list
        if num != result[-1]:  # If the current number is different from the last added
            result.append(num)
    
    return result

# E. linear_merge
def linear_merge(list1, list2):
    result = []
    i, j = 0, 0
    
    # Merge the two lists while both have elements
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # If any elements remain in list1 or list2, append them
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print()
    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])

if __name__ == '__main__':
    main()
