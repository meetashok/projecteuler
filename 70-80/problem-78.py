def pentagonal_number(k):
    return int(k*(3*k-1) / 2)

def compute_partitions(goal):
    partitions = [1]
    for n in range(1,goal+1):
        partitions.append(0)
        for k in range(1,n+1):
            coeff = (-1)**(k+1)
            for t in [pentagonal_number(k), pentagonal_number(-k)]:
                if (n-t) >= 0:
                    partitions[n] = partitions[n] + coeff*partitions[n-t]
        yield partitions[n]

def main():
    large_num = 1000000
    partitions = compute_partitions(large_num)
    i = 1
    while True:
        npartitions = next(partitions)
        if npartitions % 1000000 == 0:
            return i
        i += 1

if __name__ == "__main__":
    answer = main()
    print(answer)