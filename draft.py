def prime_numbers(lim:int):
    nums = [i for i in range(3, lim + 1, 2)]
    print(nums)
    indexlist = []
    index = 0
    while (index < len(nums)):

        for i in range(index + 1, len(nums)):
            if nums[i] % nums[index] == 0:
                indexlist.append(i)

        index += 1

    # index = 0
    # while (index < len(indexlist)):
    #     si = index + 1
    #     while si < len(indexlist):
    #         if indexlist[si] == indexlist[index] :
    #             indexlist.remove(si)
    #         else:
    #             si += 1

    #     index += 1

    indexlist.sort(reverse=True)
    return indexlist

print(prime_numbers(50))