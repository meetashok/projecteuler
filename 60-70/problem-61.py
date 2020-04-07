## Problem 61
## Cyclical figurate numbers

def polygonal(n, order):
    if order == 3:
        return n * (n + 1) / 2
    elif order == 4:
        return n * n
    elif order == 5:
        return n * (3*n - 1) / 2
    elif order == 6:
        return n * (2*n - 1)
    elif order == 7:
        return n * (5*n - 3) / 2
    elif order == 8:
        return n * (3*n - 2)
    else:
        return "error"

def generate_polygonal(order):
    n = 1
    resultant_set = []
    condition = True
    while condition:
        p = polygonal(n, order)
        if p > 9999:
            condition = False
        if (p > 999) & (p < 10000):
            if (str(p)[2] != "0"):
                resultant_set.append(p)
        n += 1
    return resultant_set

p_3 = generate_polygonal(3)
p_4 = generate_polygonal(4)
p_5 = generate_polygonal(5)
p_6 = generate_polygonal(6)
p_7 = generate_polygonal(7)
p_8 = generate_polygonal(8)

def halves(p):
    first_half = []
    second_half = []
    for number in p:
        f = int("".join(str(number)[0:2]))
        s = int("".join(str(number)[2:]))
        first_half.append(f)
        second_half.append(s)
    return (first_half, second_half)

p_3f, p_3s = halves(p_3)
p_4f, p_4s = halves(p_4)
p_5f, p_5s = halves(p_5)
p_6f, p_6s = halves(p_6)
p_7f, p_7s = halves(p_7)
p_8f, p_8s = halves(p_8)

def find_in_next(numbers, series):
    series_f, series_s = halves(series)
    t = [b[-1] for b in numbers]
    t_f, t_s = halves(t)
    result = []
    for number_f, number_s, _, number in zip(t_f, t_s, t, numbers):
        for s_f, s_s, s in zip(series_f, series_s, series):
#             print number, s
            if number_s == s_f:
                result.append((number, s))  
    return result

t = [(n,) for n in p_8]

import itertools
c = itertools.permutations([p_3, p_4, p_5, p_6, p_7], 5)
for c_next in c:
    k = find_in_next(find_in_next(find_in_next(find_in_next(find_in_next(find_in_next(t, c_next[0]), c_next[1]), c_next[2]), c_next[3]), c_next[4]), p_8)
    if k != []:
        print k, "\n"