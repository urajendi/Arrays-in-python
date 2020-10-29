'''
	Problem: Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
    Constraints:
        0 <= nums.length <= 3 * 104
        -104 <= nums[i] <= 104
        nums is sorted in ascending order
'''
from typing import List
    
def removeDuplicates(nums: List[int]) -> int:
    '''
        Time complexity: O(n)
        Space complexity: O(1)
    '''
    n = len(nums)
    i = n-1
    while (i>0):
        if nums[i]==nums[i-1]:
            nums.remove(nums[i])
            n -= 1
        i -= 1
    print("Output Array =", nums)
    print("Length of output array =", n)
    return n
        
def main ():
    '''
        nums - Array elements (string of numbers in range [-10^4, 10^4])
    '''
    arr=[]
    print("Enter the array elements: ")
    num=input()
    for i in num.split(','):
        arr.append(int(i))
    print("Array =", arr)
    n = removeDuplicates(arr)
      
if __name__ == "__main__":
    main()