class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
                if i not in "+-/*":
                    stack.append(int(i))
                else:
                    s2 = stack.pop()
                    s1 = stack.pop()
                    operandVal = 0
                    if i == "+":
                        operandVal = s1 + s2
                    elif i == "-":
                        operandVal = s1 - s2
                    elif i == "*":
                        operandVal = s1 * s2
                    elif i == "/":
                        operandVal = int(s1 / s2)
                    print(operandVal)
                    stack.append(operandVal)
        return stack.pop()
        