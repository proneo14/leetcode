class Solution:
    def countBits(self, n: int) -> List[int]:
        
        output = [0]

        for i in range(1, n + 1):
            count = 0
            if (i % 2) == 0:
                count += output[(i // 2)]
            else:
                count += output[(i // 2)] + 1
    
            output.append(count)

        return output