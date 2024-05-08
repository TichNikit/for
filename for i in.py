# цикл с машинами
cars_list = ["BMW", "MB", "LADA", "KIA", "HONDA"]

for i in cars_list:
    print(f'Я езжу на автомабиле марки {i}')

print('\nА теперь шаг №2\n')
#цикл с машинами и сложением
cars_count = 0

for i in range(len(cars_list)):
    print(f'Я езжу на автомабиле марки {cars_list[i]}')
    cars_count +=10

print(cars_count)


