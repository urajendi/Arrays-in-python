'''
	Problem: Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
    Note:
        1 <= A.length <= 10000
        -10000 <= A[i] <= 10000
        A is sorted in non-decreasing order.
'''
from typing import List
    
def sortedSquares(A: List[int]) -> List[int]:
    '''
        Time complexity: O(nlogn)
        Space complexity: O(1)
    '''
    return sorted(a*a for a in A)
        
def main ():
    '''
        n - Array size (int): 1 <= n <= 10000
        temp - Array elements (string of numbers separated by ' ')
    '''
    arr=[]
    print("Enter the array elements: ")
    temp=input()
    for i in temp.split():
        arr.append(int(i))
    n = len(arr)
    print("Array size = ", n)
    print("Array = ", arr)
    result = sortedSquares(arr)
    print("Sorted squares array: ", result)
      
if __name__ == "__main__":
    main()
