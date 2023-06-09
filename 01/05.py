'''Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.'''

revenue = int(input('Введите выручку фирмы: '))
expenses = int(input('Введите издержки фирмы: '))

if revenue > expenses:
    print('Выручка больше издержек')
    profit = revenue - expenses
    profitability = profit / revenue
    print('Рентабельность выручки - ', profitability)
    workers = int(input('Введите количество сотрудников фирмы: '))
    prof_workers = profit / workers
    print('Прибыль в расчете на одного сторудника сотавила:', prof_workers)
elif revenue == expenses:
    print('Выручка равна издержкам')
else:
    print('Издержки больше выручки')