def Fibonacci(n):
    lst = [0]
    if n == 0:
        return lst
    
    f1 = 0
    f2 = 1
    lst = lst + [1]

    # Form right(positive) part
    for i in range(2, n + 1):
        lst = lst + [f1 + f2]
        f1 = f2
        f2 = lst[i]
    
    f1 = lst[0]
    f2 = lst[1]
    
    #Form left(negative-positive) part
    for i in range(1, n + 1):
        lst = [f2 - f1] + lst
        f2 = f1
        f1 = lst[0]
    
    return lst



st = input('Enter integer positive number : ')
while not st.isdigit():
    st = input('Enter integer positive number : ')

k = int(st)

print(Fibonacci(k))