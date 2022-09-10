def DecToBin(dec):
    '''Перевод целого числа из десятичной системы счисления в двоичную
    '''
    bin = ''
    while True:
        bin = str(dec % 2) + bin
        dec //= 2
        if dec == 0:
            break
    
    return bin

st = input('Enter integer positive number : ')
while not st.isdigit():
    st = input('Enter integer positive number : ')

num = int(st)

print('Answer is : ', DecToBin(num))