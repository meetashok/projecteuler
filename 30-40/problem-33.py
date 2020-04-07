## Problem 33
## Digit cancelling fractions

import numpy as np
import functools

def main():
    numerators = np.arange(11, 100)
    denominators = np.arange(11, 100)

    non_trivials = []

    for n in numerators:
        for d in denominators[denominators > n]:
            str_n, str_d = sorted(list(str(n))), sorted(list(str(d)))
            if ("0" not in str_n) & ("0" not in str_d):
                if str_n != str_d:
                    if (str_n[0] in str_d) | (str_n[1] in str_d):
                        if str_n[0] in str_d:
                            to_remove = str_n[0]
                            str_n.remove(to_remove)
                            str_d.remove(to_remove)
                            if (n * 1.0 / d) == ((int("".join(str_n)) * 1.0) / int("".join(str_d))):
                                non_trivials.append((n, d))
                        else:
                            to_remove = str_n[1]
                            str_n.remove(to_remove)
                            str_d.remove(to_remove)
                            if (n * 1.0 / d) == ((int("".join(str_n)) * 1.0) / int("".join(str_d))):
                                non_trivials.append((n, d))
                                
    return functools.reduce(lambda x,y: (x[0]*y[0], x[1]*y[1]), non_trivials)

if __name__ == "__main__":
    answer = main()
    print(answer)