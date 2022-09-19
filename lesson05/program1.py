# Считываем текст из файла. Можно считывать из консоли
with open('test.txt','r') as f :
    txt = f.read()
txt = txt.replace('\n',' ')
print(txt)

answer = list(filter(lambda x: not 'абв' in x, txt.split(' ')))

print(' '.join(answer))
