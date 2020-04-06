## Problem 52
## Permuted multiples

condition = True
number = 2

while condition:
    number += 1
    if sorted(list(str(number*1))) == sorted(list(str(number*2))) :
        if sorted(list(str(number*2)))  == sorted(list(str(number*3))) :
            if sorted(list(str(number*3)))  == sorted(list(str(number*4))) :
                if sorted(list(str(number*4)))  == sorted(list(str(number*5))) :
                    if sorted(list(str(number*5)))  == sorted(list(str(number*6))) :
                        print number
                        condition = False