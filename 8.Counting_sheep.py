# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

# For example,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined


def count_sheeps(sheep):
    """
    This function counts the number of sheep in the given list.

    Parameters:
    sheep (list): A list of elements representing whether a sheep is present (True) or not present (False).

    Returns:
    int: The number of sheep present in the list.
    """
    
    # count = 0
    # for sheep_ in sheep:
    #     if sheep_ == True:
    #         count += 1
    # return count

    # return sum(1 for sheep_ in sheep if sheep_ == True)

    return sheep.count(True)


count = count_sheeps([True,  True,  True,  False,
                      True,  True,  True,  True ,
                      True,  False, True,  False,
                      True,  False, False, True ,
                      True,  True,  True,  True ,
                      False, False, True,  True])

print(count)