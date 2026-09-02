class Solution:
    def countBits(self, n: int) -> List[int]:
        
        output = [0]

        for i in range(1, n + 1):
            count = 0
            if (i % 2) == 0:
                count += output[(i >> 1)]
            else:
                count += output[(i >> 1)] + 1
    
            output.append(count)

        return output