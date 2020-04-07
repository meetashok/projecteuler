def main():
    '''Sum of first n natural numbers is $\frac{n(n+1)}{2}$
    Sum of squares of first n numbers is $\frac{n(n+1)(2n+1)}{6}$
    '''
    n = 100
    return n * (n+1) * (3*n**2 - n - 2) // 12

if __name__ == "__main__":
    answer = main()
    print(answer)