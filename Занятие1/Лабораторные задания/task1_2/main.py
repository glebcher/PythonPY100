TAX = 0.13
total_earn = int(input('Ваш оклад', ))
tax_from_earn = total_earn * TAX
earn_after_tax = total_earn - tax_from_earn
print('Доход после уплаты налога', earn_after_tax)
print('Уплаченный налог', tax_from_earn)