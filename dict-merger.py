my_dict1 = {}
my_dict2 = {}

total_dict = {}

#Добавление в словарь №1

while True:
    key1 = input("Введите ключ для словаря №1 (пустое поле = конец ввода): ").strip()

    if key1 == "":
        break    
    
    key_value1 = input(f"Введите значение для ключа {key1}: ")

    my_dict1[key1] = key_value1

#Добавление в словарь №2

while True:
    key2 = input("Введите ключ для словаря №2 (пустое поле = конец ввода): ").strip()

    if key2 == "":
        break    
    
    key_value2 = input(f"Введите значение для ключа {key2}: ")

    my_dict2[key2] = key_value2
#проверка на наличие ключей из первого словаря во втором ( берет из второго )
total_dict = my_dict1 | my_dict2 


print(total_dict)
         