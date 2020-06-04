def odometer(oksana):
    s = oksana[0] * oksana[1]
    for ix_v in range(2, len(oksana) - 1, 2):
        s += oksana[ix_v] * (oksana[ix_v + 1] - oksana[ix_v - 1])
    return s
