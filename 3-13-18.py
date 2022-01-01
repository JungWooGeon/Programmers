def solution(p):
    left = 0
    right = 0
    u = ''
    v = ''
    isU = True

    if right_sentence(p):
        return p

    for s in p:
        if s == '(':
            left += 1
        elif s == ')':
            right += 1
        if isU:
            u += s
        else:
            v += s
        if left != 0 and right != 0 and left == right:
            isU = False
    if right_sentence(u):
        return u + solution(v)
    else:
        u = u[1:-1]
        temp = ''
        for s in u:
            if s == '(':
                temp += ')'
            elif s == ')':
                temp += '('
        return '(' + solution(v) + ')' + temp


def right_sentence(p):
    left = 0
    right = 0
    for s in p:
        if s == '(':
            left += 1
        elif s == ')':
            right += 1
        
        if left < right:
            return False
    return True

print(solution('()))((()'))