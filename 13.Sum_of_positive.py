# Вы получаете массив чисел, возвращаете сумму всех положительных чисел.

# Пример [1,-4,7,12] => 1 + 7 + 12 = 20

# Примечание: если суммировать нечего, по умолчанию используется значение sum 0.

def positive_sum(arr):
    # return sum(num for num in arr if num > 0)
    return sum(filter(lambda x: x > 0, arr))

print(positive_sum([1,2,3,4,5]))
print(positive_sum([1,-2,3,4,5]))
print(positive_sum([-1,2,3,4,-5]))
print(positive_sum([-1,-2,-3,-4,-5]))