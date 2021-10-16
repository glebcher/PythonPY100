DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input('Ваш год рождения', ))
current_year = int(input('Какой сейчас год?', ))

days_gone = (current_year - start_year) * DAYS_OF_YEAR
print (days_gone)