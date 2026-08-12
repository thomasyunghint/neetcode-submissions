class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return False
        token=[]

        for i in tokens:
            if i not in "+-*/":
                token.append(int(i))
            elif i == "+":
                b = token.pop()
                a = token.pop()
                num = a + b
                token.append(num)
            elif i == "-":
                b = token.pop()
                a = token.pop()
                num = a - b
                token.append(num)
            elif i == "*":
                b = token.pop()
                a = token.pop()
                num = a * b
                token.append(num)
            elif i == "/":
                b = token.pop()
                a = token.pop()
                num = int(a/b)
                token.append(num)
        return token.pop()