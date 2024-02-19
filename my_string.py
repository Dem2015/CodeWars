string = "Hello World"
name = 'Dmitriy'
num = 31
print(string.strip('Hd'))
print(string.split())

last_digit = num % 10
if str(num).endswith('1'): # Пробуем новый метод. Не потому что я дурак)
    word = 'год'
elif 2 <= last_digit <= 4:
    word = 'года'
else:
    word = 'лет'

full_info = [string, name, num, word]
full_info_dict = {'string': "Всем привет", 'name': 'Дмитрий', 'num': num, 'word': word}

print("Длина строки", len(string))
print("{}, меня зовут {} и мне {} {}.".format(*full_info))
print("{string}, меня зовут {name} и мне {num} {word}.".format(**full_info_dict))


# Замена всех вхождений "apple" на "orange" в строке
s = "apple, banana, apple, cherry"
result = s.replace("apple", "orange", 1)
print(result)  # Output: orange, banana, orange, cherry

str = "Hello, world!"
index = str.find("world") # Применение метода find()
print(str[index:].capitalize())
