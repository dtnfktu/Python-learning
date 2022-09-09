def DecToBin(dec):
    if dec == 0:
        return '0'
    bin = ''
    while dec != 0:
        bin = str(dec % 2) + bin
        dec //= 2
    return bin

st = input('Enter integer positive number : ')
while not st.isdigit():
    st = input('Enter integer positive number : ')

num = int(st)

print('Answer is : ', DecToBin(num))