class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        snew = ""
        for char in s:
            if char.isalnum():
                snew += char.lower()
        
        left = 0
        right = len(snew) - 1
        while left < right:
            if snew[left] != snew[right]:
                return False
             
            left += 1
            right -= 1
        
        return True