# ЧИСЛОВЫЕ ДАННЫЕ
print (125) # выводит в консоль (число 125, можно использовать и без ковычек "").
# type () # указывает на тип данных
print (type (125)) # выводит в консоль (<class 'int'>). int - integer (переводится как "целое число")
print (125 + 125) # складывает числа.
print (125 - 125) # вычетает числа.
print (125 * 125) # умножает числа.
print (125 / 125) # делит числа.
# существует несколько способов деления: // - целочисленное деление, / - простое деление (возвращает ответ в виде дробного числа. Тип этих чисел называется float - с плавающей точкой).
print (125 // 125) # делит числа нацело!
print (125 % 125) # находит остаток от деления. Может пригодится для проверки числа на четность.
print (125 % 2) # число не четное так, как остаток от деления равен 1.
print (125 ** 2) # возведение в степень
# теже самые операции можно выполнить и для дробного числа
print (125.0)
print (type (125.0)) # выводит в консоль (<class 'float'>) и означает что число с плавающей точкой (или запятой).
print (125.0 + 125.0)
print (125.0 - 125.0)
print (125.0 * 125.0)
print (125.0 / 125.0)
print (125.0 // 125.0)
print (125.0 % 125.0)
print (125.0 % 2)
print (125.0 ** 2)

# СТРОЧНЫЕ ДАННЫЕ
# *** ВАЖНО отметить, что в языках программирования существуеют две группы данных ("изменяемые" и "не изменяемые"). Числа относятся к "не изменяемым" типам.
print ("Hellow, world!") # Выводит буквы-слова в консоль
print (type("Hellow, world!")) # выводит в консоль (<class 'str'>). От анг. string - строка.
print (' "Hellow, world!" ') # одинарные ковычки говорят, что выводить? (строку с надписью!). Двойные ковычки говорят, что это строка в двойные ковычки взята.
print (" 'Hellow, world!' ") # двойные ковычки говорят, что выводить? (строку с надписью!). Одинарные ковычки говорят, что это строка в одинарные ковычки взята.
# Строки можно складывать. Операция называется конкатенацией от анг. concatenation - сложение (сцепление).
print ('Hellow,' + 'world!') # значения данных просто "склеились". Пробела НЕТ! Отступа в консоле тоже нет.
print ('    ' + 'Hellow,' + 'world!') # значения данных просто "склеились". Пробела НЕТ! Появился отступ в начале в виде табуляции.
print ('    ' + 'Hellow, ' + 'world!') # значения данных просто "склеились". НО Пробел ЕСТЬ после "Hellow, " ! Отступ в начале в виде табуляции сохранился.
# СТРОКИ МОЖНО ТОЛЬКО СКЛАДЫВАТЬ !!! Другие математические операции делать нельзя! (-/*%...)
# print ("125" + 125) # ОШИБКА сообщает что складываются два типа данных (строка + число) и это не допустимо
print ("125" + "125") # сложил две строки (НЕ ЧИСЛА !!! СТРОКИ !!!)

# ЛОГИЧЕСКИЕ ДАННЫЕ     boolean
print(True, False) # выводит логические данные True - правда, False - лож.
print(type(True), type(False)) #выводит тип данных (<class 'bool'> <class 'bool'>) и означает, что они оба логические.
# логические типы данных используются в коде как сигналы-флаги (и для пользователя и для компьютера).
print(5 > 125) # Компьютер сам определил и вывел значение False, что означает не правду.
print(5 < 125) # Компьютер сам определил и вывел значение True, что означает правда.
print(5 > 125, 5 < 125) # (print поддерживает множественный вывод) Можно несколько значение посмотреть (первое - False, второе - True)
print('    ' + 'Hellow, ' + 'world!', 5 > 125, 5 < 125, "   ", True) # вывел разные (множество) значений через запятую " , ". Разделители " , " помогают вывести разные типы данных.
# print('    ' + 'Hellow, ' + 'world!', + 5 > 125, + 5 < 125, + "   ", + True) # вот так уже не выведит
# print('    ' + 'Hellow, ' + 'world!', + , 5 > 125, + , 5 < 125, + "   ", + True) # и так тоже не выведит
print(5 >= 125, 5 <= 125) #проверка на дольше/меньше либо ровно. ВАЖНО знак " = " ставить после знаков " > " либо " < ".
print(5 == 125, 5 == 125) # равны ли эти числа ? проверка на равенство
print(5 != 125) # проверка на не равны?! проверка на не равенство
print(5 != 125 and 5 == 125) # проверяется сложное выражение "5 != 125" (5 не равно 125) и "5 == 125" (5 равно 125). Значение будет False потому, что оператор "and" (и) является строгим!
# ему необходимо чтобы обе стороны были правдивыми на пример:
print(5 != 125 and 5 <= 125) # тогда значение будет True так, как оба условия выполнены!
print(5 != 125 or 5 == 125) # оператор " or " (или) не строгий и выдаст значение True, если хотя бы одно выражение правдиво

# ПЕРЕВОД ИЗ ОДНОГО ТИПА ДАННЫХ В ДРУГОЙ
print(int("125")) # преобразовал "125" из значения строки ("125") в тип данных число int.
print(type(int("125"))) # Осуществилась проверка в которой показан тип int а не "125" как строка <class 'int'>
# ВАЖНО!!! Для чтения кода необходимо начинать из нутри в наружу!
# int("125") - преобразует данные из строки в число
# type(int("125")) - выводит к какому типу теперь относится "125"
# print(type(int("125"))) - просто выводит готовое значение в консоль
