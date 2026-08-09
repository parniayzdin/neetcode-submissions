class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != matching[i]:
                    return False
                stack.pop()
        
        if len(stack) == 0:
            return True
        return False


        