'''
Check if the string is valid:

1. Each (  must be paired with ) and vice-versa
2. Left before right
3. * is a wildcard (could be empty)

*(()

leftCnt = 1
wildcard = 1

'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        wildcardStack = []
        leftStack = []

        for idx, i in enumerate(s):
            if i == '(':
                leftStack.append(idx)
            elif i == '*':
                wildcardStack.append(idx)
            else:
                if len(leftStack):
                    leftStack.pop()
                elif len(wildcardStack):
                    wildcardStack.pop()
                else:
                    return False 
        
        while len(leftStack):
            if len(wildcardStack) and wildcardStack[-1] > leftStack[-1]:
                wildcardStack.pop()
                leftStack.pop()
            else:
                break
        return False if len(leftStack) else True