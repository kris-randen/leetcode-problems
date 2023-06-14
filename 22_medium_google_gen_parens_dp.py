"""
22. Generate Parentheses
Medium
18.2K
740
company
Microsoft
company
Adobe
company
Apple
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

def augment(paren):
    if not paren:
        return {"()"}
    result = set()
    for i in range(len(paren)):
        if i == 0 or paren[i - 1] == ")":
            for j in range(i+1, len(paren) + 1):
                copy = paren
                copy = copy[:i] + "(" + copy[i:]
                copy = copy[:j] + ")" + copy[j:]
                result.add(copy)
    return result

def add_parens(parens):
    result = set()
    for paren in parens:
        result = result.union(augment(paren))
    return result

def generate_parens(n):
    result = {""}
    if not n:
        return result
    for i in range(n):
        result = add_parens(result)
    return result

if __name__ == '__main__':
    u = ["(())()()","((()))()","()()()()","()(())()","()((()))","()(()())","(()(()))","((()()))","(()()())","()()(())","((())())","(((())))","(()())()"]
    v = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    u.sort()
    v.sort()
    print(u)
    print(v)