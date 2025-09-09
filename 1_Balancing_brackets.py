def is_balanced(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return "NO"
    return "YES" if not stack else "NO"

print(is_balanced("[()]"))     
print(is_balanced("{[(]})"))  
print(is_balanced("{[()]}"))  
