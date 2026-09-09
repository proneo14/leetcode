class Solution:
    def sumadd(self, n: int):
        result = 0
        while n != 0:
            temp = n % 10
            n //= 10
            result += (temp**2)

        return result

    def isHappy(self, n: int) -> bool:
        num = set()
        
        while n not in num:
            num.add(n)
            n = self.sumadd(n)
            
            if n == 1:
                return True

        return False
         