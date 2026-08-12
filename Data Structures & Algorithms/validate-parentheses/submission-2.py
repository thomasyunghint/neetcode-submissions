class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}



        for c in s:
            # if in, check same style? match correct pattern?
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            #add
            else:
                stack.append(c)

        return not stack