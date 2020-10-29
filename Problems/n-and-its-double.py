'''
	Problem: Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
    Constraints:
        2 <= arr.length <= 500
        -10^3 <= arr[i] <= 10^3
'''
from typing import List
    
def checkIfExist(arr: List[int]) -> bool:
    '''
        Time complexity: O(n)
        Space complexity: O(1)
    '''
    if arr.count(0) == 1:
        arr.remove(0)
    for i in arr:
        if i * 2 in arr:
            print("N =",i,"and Double =",i*2)
            return True
    return False
        
def main ():
    '''
        nums - Array elements (string of numbers in range [-10^3, 10^3])
    '''
    arr=[]
    print("Enter the array elements: ")
    num=input()
    for i in num.split(','):
        arr.append(int(i))
    print("Array =", arr)
    n = checkIfExist(arr)
    if(n):
        print("N and its double exists")
    else:
        print("N and its double does not exist")
      
if __name__ == "__main__":
    main()