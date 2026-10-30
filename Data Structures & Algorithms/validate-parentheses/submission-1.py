class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dico = {
            ")" : "(",
             "]":"[", 
             "}":"{"
             }

        for c in s:
            if c in dico:
                if stack and stack[-1] == dico[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        