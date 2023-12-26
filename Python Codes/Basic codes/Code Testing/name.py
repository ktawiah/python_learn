def formatted_name(first_name, lastname, middle_name = ''):
    if middle_name:
        return f'{first_name} {middle_name} {lastname}'
    else:
        return f'{first_name} {lastname}'


formatted_name('Kelvin', 'Tawiah')