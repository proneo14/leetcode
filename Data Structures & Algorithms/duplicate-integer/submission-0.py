from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = defaultdict(int)
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i] = 1
        return False