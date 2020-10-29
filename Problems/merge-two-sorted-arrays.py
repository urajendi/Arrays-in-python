'''
	Problem: Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
    Constraints:
        -10^9 <= nums1[i], nums2[i] <= 10^9
        nums1.length == m + n
        nums2.length == n
'''
from typing import List
    
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    '''
        Time complexity: O(n+m)
        Space complexity: O(1)
    '''
    # pointers for nums1 and nums2
    p1 = m - 1
    p2 = n - 1

    # set pointer for nums1
    p = m + n - 1

    # while there are still elements to compare
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] =  nums1[p1]
            p1 -= 1
        p -= 1

    # add missing elements from nums2
    nums1[:p2 + 1] = nums2[:p2 + 1]
    print("Merged array =", nums1)
        
def main ():
    '''
        n, m - Array size (int)
        num1, num2 - Array elements (string of numbers in range [-10^9, 10^9])
    '''
    arr1=[]
    arr2=[]
    print("Enter the first sorted array elements: ")
    num1=input()
    print("Enter the second sorted array elements: ")
    num2=input()
    for i in num1.split(','):
        arr1.append(int(i))
    for i in num2.split(','):
        arr2.append(int(i))
    n = len(arr2)
    m = len(arr1)-n
    print("m =", m)
    print("Array-1 =", arr1)
    print("n =", n)
    print("Array-2 =", arr2)
    merge(arr1,m,arr2,n)
      
if __name__ == "__main__":
    main()