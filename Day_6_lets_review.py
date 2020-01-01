num_test_cases = int(input())

for item in range(0, num_test_cases):

    word = input()

    for element in range(0, len(word)):
        if element % 2 == 0:
            print(word[element], end='')

    print(" ", end='')

    for element in range(0, len(word)):
        if element % 2 != 0:
            print(word[element], end='')

    print("")