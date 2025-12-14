salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
month_survive = 0
while month_survive < 10:
    current_money = money_capital
    current_spend = spend
    month_survive = 0
    for month in range(10):
        if salary >= current_spend:
            pass
        else:
            need = current_spend - salary  # При нехватки зарплаты используем подушку без-ти
            if current_money >= need:
                current_money -= need
            else:
                break # Недостаточно средств
        month_survive += 1
        if month < 9:
            current_spend *= (1+increase) # Увеличение расходов
    if month_survive < 10:
        money_capital += 100
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
