class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            val = i
            if val in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if val == "+":
                    val = a + b
                elif val == "-":
                    val = a - b
                elif val == "*":
                    val = a * b
                else:
                    val = int(a / b)
            else:
                val = int(i)
            stack.append(val)

        return stack[-1]