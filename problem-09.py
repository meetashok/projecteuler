def main():
    '''Pythagorean triplets have to be of the form 
    a = 2mn
    b = m^2 - n^2
    c = m^2 + n^2
    Using a + b + c = 1000, gives m(m+n) = 500
    '''

    def pythagorean(m, n):
        a = 2*m*n
        b = m**2 - n**2
        c = m**2 + n**2

        return a, b, c

    m = 1
    while True:
        if 500 % m == 0:
            n = 500 // m - m
            a, b, c = pythagorean(m, n)

            if b > 0: # b cannot be negative
                return a*b*c
        m += 1


if __name__ == "__main__":
    answer = main()
    print(answer)
    


    