#Toluwase Afolayan
#tafol20@bu.edu

def numOccurences(n):
    """Takes integer as an input, and
    returns how many numbers less than
    or equal to n that contain the number
    '1'
    """
    
    num_occ = 0
    # failing first test
    #return 0
    
    #test 1 development
    #string_n = str(n)
    #if '1' in string_n:
    #    return 1

    #test 2 development
    #else:
    #    return 0

    # test 3 development
    #for i in range(n+1):
    #    if '1' in str(i):
    #        num_occ+=1

    #test 4, 5, & 6 development
    for i in range(n+1):
        string_n = str(i)
        i_chars = [char for char in string_n]
        for j in i_chars:
            if j == "1":
                num_occ+=1
    return num_occ

def main():
    #print(numOccurences(12))

    
    #checks if n itself should be returned
    testcase_1 = 1
    test1 = numOccurences(testcase_1)
    assert test1 == 1, "test1: n is equal to 1, should return: 1"
    print("Passed test 1")

    #checks if a number with no ones in it will return 0
    testcase_2 = 0
    test2 = numOccurences(testcase_2)
    assert test2 == 0, "test2: n is equal to 0, should return: 0"
    print("Passed test 2")

    #checks if a number that should return more than one, one will do so
    testcase_3 = 10
    test3 = numOccurences(testcase_3)
    assert test3 == 2, "test3: n is equal to 10 , should return: 2"
    print("Passed test 3")

    #checks if a number that has more than one one in one number accounts for all these ones (eg: 11, 111, etc)
    testcase_4 = 11
    test4 = numOccurences(testcase_4)
    assert test4 == 4, "test4: n is equal to 11, should return: 3"
    print("Passed test 4")

    #checking example input to confirm functionality
    testcase_5 = 17
    test5 = numOccurences(testcase_5)
    assert test5 == 10, "test5: n is equal to 17, should return: 10"
    print("Passed test 5")

    #one more for good measure
    testcase_6 = 111
    test6 = numOccurences(testcase_6)
    assert test6 == 36, "test 6: n is equal to 111, should return: 22"
    print("Passed test 6")

    

    
if __name__ == "__main__":
    main()
