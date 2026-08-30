class Solution:
    def isValid(self, s: str) -> bool:
        bm = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = []


        for c in s:
            if c in bm:
                stack.append(c)
            else:
                top = stack.pop()
                if c != bm[top]:
                    return False
        
        return len(stack) == 0