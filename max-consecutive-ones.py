'''
	Problem: Given a binary array, find the maximum number of consecutive 1s in this array.
	The input array will only contain 0 and 1.
	The length of input array is a positive integer and will not exceed 10,000
'''
from typing import List
    
def findMaxConsecutiveOnes(nums: List[int]) -> int:
    '''
        Time complexity: O(n)
        Space complexity: O(1)
    '''
    count=0
    result=0
    for num in nums:
        if num==1:
            count = count + 1
        else:
            if result < count:
                result = count
            count=0
    return max(result,count)
        
def main ():
    '''
        n - Array size (int): 0 <= n <= 10000
        temp - Array elements (string of 0s and 1s separated by ' ')
    '''
    arr=[]
    print("Enter the array elements: ")
    temp=input()
    for i in temp.split():
        arr.append(int(i))
    n = len(arr)
    print("Array size = ", n)
    print("Array = ", arr)
    maxConsecutiveOnes = findMaxConsecutiveOnes(arr)
    print("Max no. of consecutive ones in the array = ", maxConsecutiveOnes)
      
if __name__ == "__main__":
    main()