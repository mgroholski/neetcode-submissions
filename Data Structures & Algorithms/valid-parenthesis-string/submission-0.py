'''
String s contains three characters: (,*,)
* can be (, ), or an empty string


s = ((**)

leftStack = [0]
specialStack = [2,3]

s = "(((*)"

leftStack = [0]
specialStack = []

return False if there remains left or right

'''



class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        specialStack = []

        for idx, val in enumerate(s):
            if val == '(':
                leftStack.append(idx)
            elif val == "*":
                specialStack.append(idx)
            else:
                if len(leftStack):
                    leftStack.pop()
                elif len(specialStack):
                    specialStack.pop()
                else:
                    return False
        
        while len(leftStack):
            if len(specialStack) and specialStack[-1] > leftStack[-1]:
                specialStack.pop()
                leftStack.pop()
            else:
                break

        return False if len(leftStack) else True




        