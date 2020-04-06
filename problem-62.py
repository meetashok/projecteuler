## Problem 62
## Cubic permuations

from collections import defaultdict

cubes = np.array([n**3 for n in range(1,9999)])

digits = 11
start = 10**digits
end = 10**(digits + 1)
relevant_cubes = cubes[(cubes >= start) & (cubes < end)]

permutations_dict = defaultdict(list)

for relevant_cube in relevant_cubes:
    key = tuple(sorted(str(relevant_cube)))
    permutations_dict[key].append(relevant_cube) 

for value in permutations_dict.itervalues():
#     print value
    if len(value) == 5:
        print sorted(value)