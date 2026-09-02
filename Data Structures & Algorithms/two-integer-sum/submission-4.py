class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numindex = []
        for i in range(len(nums)):
            numindex.append((nums[i], i))
        numsort = sorted(numindex)

        left = 0 
        right = len(numsort) - 1

        while left < right:
            if numsort[left][0] + numsort[right][0] == target:
                return sorted([(numsort[left][1]), (numsort[right][1])])
            elif (numsort[left][0] + numsort[right][0]) > target:
                right -= 1
            else:
                left += 1
            
        return []