# Imagine you are a treasure hunter standing at one side of the river. There are n (a positive
# integer) stones on the river. They are aligned on a straight line and at the n
# th stone, there is
# treasure waiting for you. Your target is to reach the n
# th stone. For each move, you have the
# choice of either walking (move one stone ahead) or leaping (move two stones ahead). Also, you
# are not allowed to travel backwards. Design an algorithm that calculates the number of ways
# (sequences of walks/leaps) that get you to the treasure stone. You should clearly explain the
# algorithm and demonstrate the correctness of the algorithm with a complete proof.
# Here is an example. For n = 5, there are 8 ways:
# Method 1: walk → walk → walk → walk → walk
# Method 2: walk → walk → walk → leap
# Method 3: walk → walk → leap → walk
# Method 4: walk → leap → walk → walk
# Method 5: leap → walk → walk → walk
# Method 6: leap → leap → walk
# Method 7: leap → walk → leap
# Method 8: walk → leap → leap

def count_ways_recursive(n):
    # Base cases:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    # Recursive case:
    else:
        return count_ways_recursive(n - 1) + count_ways_recursive(n - 2)

# Example usage:
n = 5
ways = count_ways_recursive(n)
print(f"Number of ways to reach the {n}-th stone: {ways}")
