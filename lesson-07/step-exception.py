# Exception - исключение

# Когда прога падает ошибка, она падает с исключением

try:
    i = int(input())
    prnt (i[0])
except ValueError:
    print ('Не корректное число!')      # от самого специфичного к самому общему. Сначала ValueError, а потом просто except
except:
    print ('Любое исключение было отловлено')
finally:
    print ('Выполняется всегда!')
    
#Д-но быть всегда except и finally

# Генерирование исключеия:

raise KeyError('Мое сообщение об ошибке')

# Нужно стараться избегать исключений, использовать только если программа дальше работать не может