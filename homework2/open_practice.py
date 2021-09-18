def print_len(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as f:
        text = f.read()
        return (f'Длина файла: {len(text)}')

def count_words(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as f:
        amount_words = 0
        text = f.read()
        for word in text.split():
            amount_words +=1
        return (f'Количество слов: {amount_words}')

def write_file(file_name,new_file_name):
     with open(file_name, 'r', encoding = 'utf-8') as f:
        text = f.read()
        text = text.replace('.','!')
        
        with open(new_file_name, 'w', encoding ='utf-8') as l:
            l.write(text)

        return f'Готово! Файл {new_file_name} записан'

print(print_len('referat.txt'))
print(count_words('referat.txt'))
print(write_file('referat.txt','referat2.txt'))
