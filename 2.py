def custom_write(file_name, strings):
    result = dict()

    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(len(strings)):
            result[(i+1, f.tell())] = strings[i]
            f.write(strings[i]+'\n')

    return result


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
