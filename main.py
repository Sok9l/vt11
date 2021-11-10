from random import randrange

print("Игра Камень,Ножницы,Бумагаю"
      " Условное обозначение"
      " 1- Камень"
      " 2- Ножницы"
      " 3- Бумага")
user=int(input('Введите соответствующее число\n'))

if user == 1:
    print('Ваш выбор Камень')
if user == 2:
    print('Ваш выбор Ножницы')
if user == 3:
    print('Ваш выбор Бумага')



comp = randrange(3) + 1
if comp == 1:
    print('Выбор компа Камень\n')
if comp == 2:
    print('Выбор компа Ножницы\n')
if comp == 3:
    print('Выбор компа Бумага\n')

if comp == user:
    print('Произошла ничья!!!!\n')
elif comp == 1 and user == 2 or comp == 2 and user == 3 or comp == 3 and user == 1:
    print('Комп выиграл(\n)')
elif comp == 2 and user == 1 or comp == 3 and user == 2 or comp == 1  and user == 3:
    print('Победил ты(\n)')




