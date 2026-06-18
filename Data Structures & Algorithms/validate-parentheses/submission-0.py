class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.insert(0, i)
            elif len(stack) > 0:
                stackPop = stack.pop(0)
                if i == ')' and not stackPop == '(':
                    return False
                elif i == ']' and not stackPop == '[':
                    return False
                elif i == '}' and not stackPop == '{':
                    return False
            else: 
                return False
        return len(stack) == 0
                
