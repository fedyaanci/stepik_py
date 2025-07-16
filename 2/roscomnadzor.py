word = input() + ' запретил букву' 

letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л',
           'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
           'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
i = 0

while (word != '' and (i < len(letters)) ):
    if word != ' ':
        print(word, letters[i])
    word = word.replace(letters[i], '')
    word = word.replace('  ', ' ')
    word = word.lstrip('')
    i+=1