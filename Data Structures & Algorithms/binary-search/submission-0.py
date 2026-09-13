class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        bottom = 0
        top = len(nums) - 1

        while bottom <= top:
            guess = (top + bottom) // 2
            if nums[guess] == target:
                return guess
            elif nums[guess] < target:
                bottom = guess + 1
            else:
                top = guess - 1

        return -1