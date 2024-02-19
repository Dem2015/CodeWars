# Установка значения по умолчанию для столицы Германии, если она отсутствует в словаре
setdefault_ = countries_dict.setdefault('Germany', 'Берлин')
print(setdefault_)
del countries_dict['Russia']
setdefault_ = countries_dict.setdefault('Russia', 'Москва')
countries_dict.pop('UK', 'Нет такого ключа')
setdefault_ = countries_dict.setdefault('UK', 'Лондон')
print(countries_dict)
key1 = 'China'
print(countries_dict.get(key1, 'Нет такого ключа {}'.format(key1)))
print(countries_dict['Russia'])


from_keys = dict.fromkeys(range(1, 5), 0)
print(from_keys)

num_list_word = ['one', 'two', 'three', 'four', 'five', 'one', 'three']
num_dict = {}
for item in num_list_word:
  num_dict.setdefault(item, 0)
  num_dict[item] += 1
print(num_dict)

countries_dict_copy = countries_dict.copy()
countries_dict_copy.update(num_dict)
print(countries_dict_copy)

print({**countries_dict, **num_dict})
print(list(countries_dict.items()))