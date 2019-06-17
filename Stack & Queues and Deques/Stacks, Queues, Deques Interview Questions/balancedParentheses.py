# 20. Valid Parentheses

def balance_check(s):

    if len(s) % 2 != 0: # edge case check
        return False

    stack = []

    openings = set('({[')
    matched = set( [('(',')'), ('{','}') , ('[',']')])

    for paren in s:
        if paren in openings:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open,paren) not in matched:
                return False

    return len(stack) == 0
