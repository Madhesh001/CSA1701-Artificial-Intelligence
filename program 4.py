from itertools import permutations

# Unique letters in the puzzle
letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')

# Try all possible digit assignments
for p in permutations(range(10), len(letters)):
    S, E, N, D, M, O, R, Y = p

    # Leading letters cannot be zero
    if S == 0 or M == 0:
        continue

    # Convert words into numbers
    SEND = 1000*S + 100*E + 10*N + D
    MORE = 1000*M + 100*O + 10*R + E
    MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

    # Check the equation
    if SEND + MORE == MONEY:
        print("Solution Found!")
        print("SEND =", SEND)
        print("MORE =", MORE)
        print("MONEY =", MONEY)
        print("Letter Mapping:")
        print("S =", S)
        print("E =", E)
        print("N =", N)
        print("D =", D)
        print("M =", M)
        print("O =", O)
        print("R =", R)
        print("Y =", Y)
        break
