# https://skillsmart.ru/algo/lvl1/cb0f.html

def MassVote(N, Votes):
    if N == 1:
        return 'majority winner 1'
        
    s = sum(Votes)
    result = []
    for v in Votes:
        result.append(round(100 * v / s, 2))
    
    maxv = [-1, -1]
    for i in range(N): 
        if (result[i] > maxv[0]): 
            maxv[1] = maxv[0] 
            maxv[0] = result[i] 
        elif (result[i] > maxv[1] and result[i] != maxv[0]): 
            maxv[1] = result[i]
    
    msg = 'minority'
    if maxv[0] > 50:
        msg = 'majority'
    elif result.count(maxv[0]) > 1:
        msg = 'no winner'

    return '{} winner {}'.format(msg, result.index(maxv[0]) + 1) if msg != 'no winner' else msg
