#тимур
#руслан

choice_1 = input()
choice_2 = input()

m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
     'ножницы-ножницы': 'ничья','ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан',
     "бумага-бумага": 'ничья','бумага-камень': 'Тимур','бумага-ножницы': 'Руслан'}

form_choices = choice_1+'-'+choice_2

print(m[form_choices])