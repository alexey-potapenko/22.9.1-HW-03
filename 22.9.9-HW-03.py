# Functions
def sort(array): # Сортировка пузырьком
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def binary_search(array, numb): # Двоичный поиск для нужного индекса
    low_idx, high_idx = 0, len(array)
    while low_idx < high_idx:
        middle = (low_idx + high_idx) // 2
        if array[middle] < numb:
            low_idx = middle + 1
        else:
            high_idx = middle
    return low_idx

def NumbCheck(numb, array): # Проверка валидности номера для нашей последовательности чисел
    if numb == array[0]:
        return 1
    elif numb < array[0]:
        return 0
    elif numb > array[-1]:
        return 2
    else:
        return 3




# вод последовательности чисел  с разделением по пробелам, переводом в список и проверкой правильности введенных данных
inp_error = True
while inp_error == True: #Ловим ошибки ввода
    try:
        seq = list(map(int, input('Введите последовательность целых чисел через пробел: ').split())) # вводим последовательность чисел
    except ValueError as e:
        print("Введите только целые числа через пробел, без букв")
    else:
        inp_error = False
# Ввод числа с проверкой правильности ввода
inp_error = True
while inp_error == True:
    try:
        numb = int(input('Введите целое число: '))
    except ValueError as e:
        print('Введите целое число без букв')
    else:
        inp_error = False

# Код
seq = sort(seq)
match NumbCheck(numb, seq): # Вывод результата
    case 0:
        print(f'Введенное число {numb} меньше любого числа в последовательности чисел {seq}.')
    case 1:
        print(f'Введенное число {numb} является первым в последовательности чисел {seq}.')
    case 2:
        print(f'Введенное число {numb} больше любого числа в последовательности чисел {seq}.')
    case _:
        pos = binary_search(seq, numb)
        print(f'Введенное число {numb} больше элемента {pos - 1} и меньше или равен элементу {pos} в последовательности чисел {seq}.')





