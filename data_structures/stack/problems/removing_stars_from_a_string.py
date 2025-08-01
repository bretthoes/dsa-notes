class Solution:
    def removeStars(self, s: str) -> str:
        # create an empty stack
        # iterate thru forwards
        # if current char is not *, append to stack
        # if current char is *, pop from stack
        stack = []
        for char in s:
            if char == '*' and stack:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


        
