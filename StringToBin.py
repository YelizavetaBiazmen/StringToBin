print('Введите строку для перевода в двоичную систему.')
name = input()
binName = ''   # переменная для хранения результата  
for char in name: # цикл по символам (char) строки(name)
    decCode = ord(char) # код символа char
    binCode = bin(decCode) # конвертируем в двоичную систему
    sBinCode = binCode[2:] # убираем 0b из начала строки
    binName = binName + sBinCode # дописываем код в конец переменной
    print(char, ' - ', decCode, ' - ', sBinCode)
print('результат:', binName)
