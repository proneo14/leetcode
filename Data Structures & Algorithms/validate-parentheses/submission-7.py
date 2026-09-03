class Solution:
    mapping  = {")" : "(", "}" : "{", "]" : "[",}
    def isValid(self, s: str) -> bool:
        stack = []
        

        for p in s:
            if p in self.mapping:
                if (not stack) or (stack[-1] != self.mapping[p]):
                    return False
                stack.pop()
            else:
                stack.append(p)

        return (not stack)