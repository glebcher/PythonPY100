time_per_task = int(input()) # Напишите ваше решение
if time_per_task * 10 > 60:
    print('Часов было потрачено на выполнение ДЗ: ', (time_per_task * 10) // 60)
else: print('На выполнение дз было затрачено меньше часа')