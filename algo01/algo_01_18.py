# https://skillsmart.ru/algo/lvl1/f27e.html

# string BiggerGreater(string input)

def BiggerGreater(input):
    for el in all_perms(sorted(input)):
        el = ''.join(el)
        if el > input:
            return el
    return ''


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for (index, first_elmt) in enumerate(elements):
            other_elmts = elements[:index]+elements[index+1:]
            for permutation in all_perms(other_elmts): 
                yield [first_elmt] + permutation
