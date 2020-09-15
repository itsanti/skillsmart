# https://skillsmart.ru/algo/lvl1/f70a.html

# string BalancedParentheses(int N)


def BalancedParentheses(N):
    return ' '.join(gen(0, 0, N, [], ''))


def gen(open, close, N, acc, out):
    if open == N and close == N:
        acc.append(out)
    else:
        if open < N:
            gen(open + 1, close, N, acc, out + '(')
        if close < open:
            gen(open, close + 1, N, acc, out + ')')
    return acc
