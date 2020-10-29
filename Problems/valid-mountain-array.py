'''
	Problem: Given an array A of integers, return true if and only if it is a valid mountain array.
    Note:
        A is a mountain array if and only if: A.length >= 3
        0 <= A.length <= 10000
        0 <= A[i] <= 10000 
'''
from typing import List
    
def validMountainArray(A: List[int]) -> bool:
    '''
        Time complexity: O(n)
        Space complexity: O(1)
    '''
    # Case-1: A is empty or has only 2 elements
    if len(A) < 3:
        return False

    n = len(A)
    peak = max(A)
    isValid = True
    i = 0

    # Case-2: First element is the peak
    if A[i] == peak:
        return False

    # Case-3: If there are more than 1 peak
    if A.count(peak)>1:
        return False

    # Check for strict increase until peak
    while A[i] != peak:
        if not (A[i]<=A[i+1]):
            return False
        i += 1

    # Case-4: Last element is the peak
    if i == n-1:
        return False

    # Check for strict decrease until last element of A
    while i != n-1:
        print(A[i], A[i+1])
        if(A[i]<=A[i+1]):
            return False
        i += 1
    return isValid
        
def main ():
    '''
        nums - Array elements (string of numbers in range [0, 10^4])
    '''
    arr=[]
    print("Enter the array elements: ")
    num=input()
    for i in num.split(','):
        arr.append(int(i))
    print("Array =", arr)
    n = validMountainArray(arr)
    if(n):
        print("It is a valid mountain array")
    else:
        print("It is not a valid mountain array")
      
if __name__ == "__main__":
    main()