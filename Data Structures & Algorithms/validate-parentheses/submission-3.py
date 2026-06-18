class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if stack:
                    c = stack.pop()
                    if i == ")" and c != "(":
                        return False
                    elif i == "}" and c != "{":
                        return False
                    elif i == "]" and c != "[":
                        return False
                else:
                    return False

        return len(stack) == 0
        