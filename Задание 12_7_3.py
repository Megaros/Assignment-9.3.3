per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit=[] 
def example():

    # Бесконечный цикл, который продолжает выполняться  
    # до возникновения исключения
    while True:
        global money
        try:
            money = int(input("Введите сумму (только целым числом) которую планируете вложить под %:" ))

        # Если полученный ввод не число, будет вызвано исключение
        except ValueError:
            # Цикл будет повторяться до правильного ввода
            print("Error! Это не число, попробуйте снова.")

        # При успешном преобразовании в целое число,  
        # цикл закончится.
        else:
            break

# Вызываем функцию
example()

interest_rate=list(per_cent.values())
for i in range(len(per_cent)):
    dep = round(interest_rate[i]*money/100,1)
    deposit.append(dep)
print('deposit =',deposit)
max_bank=max(per_cent, key=per_cent.get)
print('Максимальная сумму можете получить в банке', max_bank, 'Она составит: ','Ваш депозит увеличиться к концу года на',max(deposit), 'руб')

  
