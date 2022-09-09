import math
import random

def CreateRandomList(ListLen = 10, MinNum = 0, MaxNum = 25): 
    ''' The method generates a list of random floats of a given length ListLen (default = 10)
    The numbers take a value from MinNum (default = 0) to MaxNum (default = 25)
    '''
    NewList = [round(random.random() * 100, 3) for i in range(ListLen)]
    return NewList


def GetMaxFractionalPart(List):
    max = List[0] - int(List[0])
    for i in range(1, len(List)):
        t = List[i] - int(List[i])
        if max < t:
            max = t
    return max

def GetMinFractionalPart(List):
    min = List[0] - int(List[0])
    for i in range(1, len(List)):
        t = List[i] - int(List[i])
        if min > t:
            min = t
    return min    

AList = CreateRandomList()
print(AList)

print(f'Max = {GetMaxFractionalPart(AList):.3f}, Min = {GetMinFractionalPart(AList):.3f}')
print('Max - Min = {:.3f}'.format(GetMaxFractionalPart(AList)-GetMinFractionalPart(AList)))