import random

def sockMerchant(n, arr):
    # Write your code here
    dictionary = {}
    duplicates = 0

    for numb in arr:
        if numb not in dictionary:
            dictionary[numb] = 1
        else:
            dictionary[numb] += 1
            
    for y in dictionary.values():
        if y % 2 != 0:
            duplicates += (y - 1) / 2
        else:
            duplicates += y / 2

    print(int(duplicates))

    
sockMerchant(7,[1,1,2,2,3,3,4,5,])


def first_test_array():
    return sockMerchant(30,random.sample(range(1,40),10 ) + (random.sample(range(50,100),10 ))*2)

first_test_array()


def second_test_array():
    return sockMerchant(80,random.sample(range(1,12),8) + (random.sample(range(60,100),36))*2)

second_test_array()


l = random.sample(range(1,10),8) + (random.sample(range(70,120),36))*2

print(len(l))

