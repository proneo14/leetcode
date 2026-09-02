class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in nummap:
                return sorted([i, nummap[complement]])

            nummap[nums[i]] = i

        return []