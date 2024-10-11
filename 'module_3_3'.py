def print_params(a = 1, b = 'строка', c = True):
    print(a, b , c)
print_params()
print('.................................')
print_params(4, 'линия', False)
print_params(5,"Лист")
print_params(a = "Пять", b = 'Три', c = 'Два' )
print_params(a = "Пять", b = 'Три')
print_params(a = "Пять",)
print_params(b = 'Три')
print_params(c = 'Два')
print_params()
print('..................................')
print_params(b = 25)
print_params(c = [1,2,3])
print('..................................')
values_list = [10, 'Petr', False]
values_dict = {'a': 4, 'b': True, 'c': 'seven'}
print_params(*values_list)
print_params(**values_dict)
print('..................................')
values_list_2 = [12.5, "'seven'"]
print_params(*values_list_2, 42)