'''
	Problem: Given an array nums and a value val, remove all instances of that value in-place and return the new length.
    Constraints:
        0 <= nums.length <= 100
        0 <= nums[i] <= 50
        0 <= val <= 100
'''
from typing import List
    
def removeElement(nums: List[int], val: int) -> int:
    '''
        Time complexity: O(n)
        Space complexity: O(1)
    '''
    n = len(nums)
    i = n-1
    while (i>-1):
        if nums[i]==val:
            nums.remove(nums[i])
            n -= 1
        i -= 1
    print("Output Array -", nums)
    print("Length of output array =", n)
    return n
        
def main ():
    '''
        val - Int in the range [0,100]
        nums - Array elements (string of numbers in range [0, 50])
    '''
    arr=[]
    print("Enter the array elements: ")
    num=input()
    print("Enter the value to be removed from the array: ")
    val=int(input())
    for i in num.split(','):
        arr.append(int(i))
    print("Array =", arr)
    print("Value to remove =", val)
    n = removeElement(arr, val)
      
if __name__ == "__main__":
    main()