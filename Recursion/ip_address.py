#!/usr/bin/env python3

# Mock 5

def isValid(sub):
    if len(sub) == 1:
        return True
    if len(sub) > 3:
        return False
    if sub[0] == '0':
        return False

    return int(sub) < 256

def dfs(s, stack, pos, output):

    if len(stack) == 4:
        if pos == len(s):
            output.append(".".join(stack))
        return

    for i in range(1,4):
        sub = s[pos:pos+i]
        if isValid(sub):
            stack.append(sub)
            dfs(s, stack, pos+i, output)
            stack.pop()
        else:
            break

def get_ips(s):
    output = []
    stack = []

    dfs(s, stack, 0, output)

    print(output)

get_ips("1921680201")
