def ConquestCampaign(N, M, L, battalion):
    s = 0
    days = 1
    field = [[0] * M for row in range(N)]
    next_day = []
    
    for n in range(0, L * 2 - 1, 2):
        if field[battalion[n] - 1][battalion[n + 1] - 1] == 0:
            field[battalion[n] - 1][battalion[n + 1] - 1] = 1
            next_day.append((battalion[n], battalion[n + 1]))
            s += 1

    if s == N * M:
        return days

    while s < N * M:
        tmp_day = []
        for cell in next_day:
            tmp_day.extend(fill_cells(N, M, field, cell))
        next_day = tmp_day
        s += len(tmp_day)
        days += 1

    return days

def fill_cells(N, M, field, cell):
    result = []
    
    if cell[0] - 1 > 0 and field[cell[0] - 2][cell[1] - 1] == 0:
        field[cell[0] - 2][cell[1] - 1] = 1
        result.append((cell[0] - 1, cell[1]))
    
    if cell[0] + 1 <= N and field[cell[0]][cell[1] - 1] == 0:
        field[cell[0]][cell[1] - 1] = 1
        result.append((cell[0] + 1, cell[1]))

    if cell[1] - 1 > 0 and field[cell[0] - 1][cell[1] - 2] == 0:
        field[cell[0] - 1][cell[1] - 2] = 1
        result.append((cell[0], cell[1] - 1))    
    
    if cell[1] + 1 <= M and field[cell[0] - 1][cell[1]] == 0:
        field[cell[0] - 1][cell[1]] = 1
        result.append((cell[0], cell[1] + 1))     
    
    return result
