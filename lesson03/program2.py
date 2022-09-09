import random

def CreateRandomList(ListLen = 10, MinNum = 0, MaxNum = 25): 
    ''' The method generates a list of random integers of a given length ListLen (default = 10)
    The numbers take a value from MinNum (default = 0) to MaxNum (default = 25)
    '''
    NewList = [random.randint(MinNum, MaxNum) for i in range(ListLen)]
    return NewList

def CountMultiplicationOfPairNumbers(AList):
    res = []
    LeftIndex = 0
    RightIndex = len(AList) - 1
    while LeftIndex <= RightIndex:
        res.append(AList[LeftIndex] * AList[RightIndex])
        LeftIndex += 1
        RightIndex -= 1
    return res

List = CreateRandomList(ListLen = random.randint(1, 10))
print('Considering list :')
print(List)

print('The resulting list')
print(CountMultiplicationOfPairNumbers(List))