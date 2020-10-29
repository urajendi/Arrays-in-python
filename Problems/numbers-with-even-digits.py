'''
	Problem: Given an array nums of integers, return how many of them contain an even number of digits.
    Constraints:
        1 <= nums.length <= 500
        1 <= nums[i] <= 10^5
'''
from typing import List
    
def findNumbersWithEvenDigits(nums: List[int]) -> int:
    '''
        Time complexity: O(n)
        Space complexity: O(1)
    '''
    count=0
    for num in nums:
        if ((num>9 and num<100) or (num>999 and num<10000) or num==100000):
            count = count+1
    return count
        
def main ():
    '''
        n - Array size (int): 1 <= n <= 100000
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
    numbersWithEvenDigits = findNumbersWithEvenDigits(arr)
    print("Count of numbers with even digits = ", numbersWithEvenDigits)
      
if __name__ == "__main__":
    main()