# The provided code stub reads and integer, n, from STDIN.
# For all non-negative integers , i < n print i ** 2 .
# The list of non-negative integers that are less than n = 3 is [0,1,2].
# Print the square of each number on a separate line.


if __name__ == '__main__':
    n = int(input())


for i in range(0,n):
    i = i ** 2
    n = n - 1
    print(i)