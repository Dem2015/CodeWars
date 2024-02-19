list_ = ['one', 'two', 'three', 'four', 'five']
six = 'six'
list_.append(six)
list_.insert(0, 'zero')
list_.insert(len(list_), 'seven')
list_[len(list_):] = ['eight', 'nine']
# list_.remove('nine')
# list_.pop() 

print(list_)
print(len(list_) )

# Конкатенация списков
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

my_list3 = my_list1 + my_list2

# Повторение списка
my_list4 = my_list1 * 3

# Проверка принадлежности элемента списку
is_in = 2 in my_list1
print(is_in)

# Проверка не принадлежности элемента списку
is_not_in = 7 not in my_list1
print(is_not_in)

# Вывести списки
print(my_list3)  # Выводит [1, 2, 3, 4, 5, 6]
print(my_list4)  # Выводит [1, 2, 3, 1, 2, 3, 1, 2, 3]

list5 = []
for i in range(10):
  list5.append(i)
print(list5)
list5 = [i for i in range(10)]
print(list5)

list6 = list(range(10))
print(list6)

my_dict = dict(zip(list_, list6))
print(my_dict)

print(list(my_dict))

print(my_dict.keys())
print(my_dict.values())

print(my_dict['one'])
print(my_dict.get('nine', 'Нет такого ключа'))

countries_dict = dict.fromkeys(['Russia', 'USA', 'UK'], 'undefined')
print(countries_dict)



