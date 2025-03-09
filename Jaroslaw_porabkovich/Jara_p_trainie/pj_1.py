def calculate_area(shape, a, b):
    if shape == 'прямоугольник':
        res = a * b
        print(f"Площадь прямоугольника: {res}")
    else:
        print('Ошибка: неизвестная фигура')


# Ввод данных
shape = input('Введите фигуру: ')
side_a = float(input('Длина стороны "a": '))
side_b = float(input('Длина стороны "b": '))
calculate_area(shape,side_a,side_b)
print('продолжение следует...')
print()