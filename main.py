# Домашнее задание по теме "Обработка исключений".
# Цель задания:
#
# Освоение обработки исключений в Python для улучшения надёжности и отказоустойчивости программ. Научиться обрабатывать
# исключения, включая SyntaxError, NameError, TypeError, ZeroDivisionError, IOError, ValueError, и общее исключение Exception.
# Понять применение блоков try, except, else, finally в различных сценариях.
#
#
#
# Задание:
#
# Добавление обработки исключений. К данным функциям добавить как минимум одну обработку указанных типов исключений:
# def string_to_int(s): # добавить обработку ValueError
#    return int(s)
# def read_file(filename): # добавить обработку FileNotFoundError, IOError
# with open(filename, 'r') as file:
#    return file.read()
# def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
#     return a / b
# def access_list_element(lst, index): # добавить обработку IndexError, TypeError
#     return lst[index]

def string_to_int(s):  # добавить обработку ValueError
    try:
        return int(s)
    except ValueError:
        return f"Ошибка: невозможно преобразовать '{s}' в целое число."
print('Process finished')

def read_file(filename): # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file: return file.read()
    except FileNotFoundError:
        return f"Ошибка: файл '{filename}' не найден."
    except IOError:
        return f"Ошибка ввода/вывода при работе с файлом '{filename}'."
print('Process finished')

def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError:
        return f"Ошибка: деление на ноль."
    except TypeError:
        return f"Ошибка: аргументы должны быть числами."
print('Process finished')

def access_list_element(lst, index): # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        return f"Ошибка: индекс {index} вне диапазона списка."
    except TypeError:
        return f"Ошибка: индекс должен быть целым числом."
print('Process finished')
