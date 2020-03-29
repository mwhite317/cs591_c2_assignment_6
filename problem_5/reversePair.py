#reverse pair

#junhlei@bu.edu
def main():
    #test 2 known output first
    testcase1 = [1,3,2,3,1]
    test1 = reversePairs(testcase1)
    assert test1 == 2, "test1 array of [1,3,2,3,1] should be 2"
    
    testcase2 = [2,4,3,5,1]
    test2 = reversePairs(testcase2)
    assert test2 == 3, "test2 array of [2,4,3,5,1] should be 3"
    
    testcase3 = [2, 5]
    test3 = reversePairs(testcase3)
    assert test3 == 0, "test3 array of [2,5] should be 0"
    
    testcase4 = [5, 2]
    test4 = reversePairs(testcase4)
    assert test4 == 1, "test4 array of [5,2] should be 1"
    
    testcase5 = [1]
    test5 = reversePairs(testcase5)
    assert test5 == 0, "test5 array of [1] should be 0"
    
    testcase6 = []
    test6 = reversePairs(testcase6)
    assert test6 == 0, "test6 array of [] should be 0"
    
    testcase7 = [3, 2, 9, 2, 22, 19, 9, 2]
    test7 = reversePairs(testcase7)
    assert test7 == 7 ,"test7 array of [3, 2, 9, 2, 22, 19, 9, 2] should be 7"
    print(str(testcase1) + " " + str(testcase2) + " " + str(testcase3)+ " " + str(testcase4) + str(testcase5) + " passed")
    print(str(testcase6) + " " + str(testcase7) + " passed")
#takes in an array and counts important pairs any index i in the lower bound of the array that has a value of any index
#after (i < some j index) S.T num[i] > 2*num[j] will increment the return count by 1
def reversePairs(arr):
    if arr == []:
        return 0
    if len(arr) <= 1:
        return 0
    else:
        rec = 0
        for i in range(1, len(arr)):
            if (arr[0] > 2*arr[i]):
                rec += 1
                #print(rec)
        return rec + reversePairs(arr[1:])
    
##    if arr == [1,3,2,3,1]:
##        return 2
##    if arr == [2,4,3,5,1]:
##        return 3
##    if len(arr) == 1:
##        return 0
##    if arr[0] > 2*arr[1]:
##        return 1
##
##    rec = 0
##    for i in range(1, len(arr)):
##        if (arr[0] > 2*arr[i]):
##            rec += 1
##        return rec
##    else:
##        return 0
##    rec = 0
##    for k in range(len(arr)):
##        for i in range(k, len(arr)):
##          if (arr[0] > 2*arr[i]):
##              rec += 1
##          return rec
##    this one also works but use recursion just cause
        
    
##    else:
##        return 0
    #return 0




#runs main() with tests in it
main()
