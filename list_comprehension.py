
#8.List Comprehension
#a) Generate positive list of numbers from a given list of integers
#b) Square of N numbers
#c) Form a list of vowels selected from a given word
#d) List ordinal value of each element of a word 
a=[int(x) for x in input("enter list of integers").split()]
print(f"positive integers are{[x for x in a if x > 0]}")
print(f"the squares are{[x*x for x in a]}")
vowels = 'aeiouAEIOU'

sentence = input("Enter a string: ")
sentence_vowels = ', '.join([x for x in sentence if x in vowels])
print("Vowels in sentence are:", sentence_vowels)

word = input("Enter a word: ")
word_ord = [ord(x) for x in word]
print("ord values of letters are", word_ord)