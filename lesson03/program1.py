import random

def CreateRandomList(ListLen = 10, MinNum = 0, MaxNum = 25): 
    ''' The method generates a list of random integers of a given length ListLen (default = 10)
    The numbers take a value from MinNum (default = 0) to MaxNum (default = 25)
    '''
    NewList = [random.randint(MinNum, MaxNum) for i in range(ListLen)]
    return NewList

def GetSumInOddPosition(AList):
    '''The loop summarizes the elements at odd positions of a given list.
    The step in the cycle is 2 - only the necessary elements are selected without checking for the parity of the position, the passage through the list is twice as fast.
    '''
    summa = 0
    numPos = 1
    while numPos <= len(AList):
        summa += AList[numPos]
        numPos += 2
    return summa

List = CreateRandomList()
print('Considering list:')
print(List)

print('Sum of elements in odd positions =', GetSumInOddPosition(List))
