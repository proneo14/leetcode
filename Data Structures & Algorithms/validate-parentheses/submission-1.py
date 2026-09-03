class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if not stack:
                stack.append(p)
            elif p == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif p == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif p == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return (not stack)