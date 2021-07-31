import sys
digit_string = sys.argv[1]
n = int(digit_string)
for i in range(n):
    if i != n-1:
        print(' ' * (n-i-1) + '#' * (i+1))
    else:
        print(' ' * (n-i-1) + '#' * (i+1))
