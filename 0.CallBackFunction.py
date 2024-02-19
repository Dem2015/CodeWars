# Задача: Вычисление суммы чисел списка

# Напишите функцию calculate_sum, которая принимает список чисел и callback-функцию в качестве аргументов. Функция calculate_sum должна применить callback-функцию к каждому элементу списка и вернуть сумму результатов.

def square(x):
    return x ** 2

def cube(x):
    return x ** 3
def calculate_sum(numbers, callback):
    # sum_ = 0
    # for num in numbers:
    #     sum_ += callback(num)
    return sum(callback(num) for num in numbers)
    

numbers = [1, 2, 3, 4, 5]
print("Сумма квадратов чисел:", calculate_sum(numbers, square))  # Ожидаемый результат: 55
print("Сумма кубов чисел:", calculate_sum(numbers, cube))  # Ожидаемый результат: 225



# Задача: Фильтрация положительных чисел
# Напишите функцию filter_positive, которая принимает список чисел и callback-функцию в качестве аргументов. Функция filter_positive должна применить callback-функцию к каждому элементу списка и вернуть новый список, содержащий только те числа, для которых callback-функция вернула True.

def is_even(x):
    return x % 2 == 0

def is_positive(x):
    return x > 0

def filter_positive(numbers, callback):
    return [num for num in numbers if callback(num)]

numbers = [1, -2, 3, -4, 5, -6]
print("Положительные числа:", filter_positive(numbers, is_positive))  # Ожидаемый результат: [1, 3, 5]
print("Четные числа:", filter_positive(numbers, is_even))  # Ожидаемый результат: [-2, -4, -6]


# Задача: Преобразование строк
# Напишите функцию transform_strings, которая принимает список строк и callback-функцию в качестве аргументов. Функция transform_strings должна применить callback-функцию к каждой строке списка и вернуть новый список, содержащий преобразованные строки.

def capitalize_string(s):
    return s.capitalize()

def reverse_string(s):
    return s[::-1]

def transform_strings(strings, callback):
    # return list(map(lambda x: callback(x), strings))
    # return [callback(str) for str in strings]
    return list(map(callback, strings))

strings = ["hello", "world", "python"]
print("Преобразованные строки (заглавные буквы):", transform_strings(strings, capitalize_string))  
# Ожидаемый результат: ['Hello', 'World', 'Python']

print("Преобразованные строки (обратный порядок):", transform_strings(strings, reverse_string))  
# Ожидаемый результат: ['olleh', 'dlrow', 'nohtyp']
