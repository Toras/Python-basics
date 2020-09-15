def my_div(d1, d2):
    try:
        result = d1/d2
        return result
    except ZeroDivisionError as err:
        return err


print(f'{my_div(float(input("Введите делимое: ")),float(input("Введите делитель: ")))}')
