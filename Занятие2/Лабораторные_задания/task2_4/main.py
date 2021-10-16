if __name__ == "__main__":
    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать их


    phrase = 'Hello,world'
    hi = len(phrase)
    count_stairs = range(hi)
    offset = 5

    for index in count_stairs:
        print(' ' * (index + offset), phrase[index])

 #rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
 #for index, value in enumerate(rus_alphabet, start=1):  # TODO как за один раз получать пару индекс-значение?
        #print(index, value)