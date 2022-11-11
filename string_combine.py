#19.Create a single string seprated with space from 2 strings by swapping the character at position 1
first = list(input("Enter first string: "))
second = list(input("Enter second string: "))

first[0], second[0] = second[0], first[0]
final = ''.join(first) + ' '  +  ''.join(second)

print(final)