# https://skillsmart.ru/algo/lvl1/a9d8.html

# L = road length
# N = stoplight count
# track = [[1,2,3], [1,2,3]] road description
#   [free_road, red_light, green_light]

def Unmanned(L, N, track):
    cur_t = 0
    wait_t = 0
    
    for part in track:
        cur_t += part[0] - cur_t
        
        if cur_t > L:
            break
        
        awt = part[1] - (cur_t + wait_t) % (part[1] + part[2])
        
        if awt > 0:
            wait_t += awt
    
    return L + wait_t
