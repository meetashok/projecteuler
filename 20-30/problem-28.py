## Problem 28
## Number spiral diagonals

def main():
    size = 1001
    grid = range(1, size**2+1)
    layer = []

    for i in range(0, size, 2):
        index = i + 1
        if index == 1:
            low = 1
        else:
            low = ((index-2)**2 + 1)
        high = (index)**2
        layer.append(grid[low-1:high])
        
    summation = 0

    for i in range(1,(size+1) // 2):
        values = layer[i]
        side_length = 2*(i+1) - 1
        selected = values[side_length - 2::(side_length - 1)]
        summation += sum(selected)

    return summation + 1

if __name__ == "__main__":
    answer = main()
    print(answer)