'''
tokens = ["2","1","+","3","*"]

stack = [3, 3]
res = 9

tokens = ["4","13","5","/","+"]
stack = [6]


'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+-*/":
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(b - a)
                elif i == "/":
                    stack.append(int(b / a))
                elif i == "*":
                    stack.append(a * b)
            else:
                stack.append(int(i))

        return stack[0]
        