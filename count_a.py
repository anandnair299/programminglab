#11. Store a list of first name, count occurance of 'a' within the list
name_sent = input("Enter a list of first names seperated by spaces: ")
name_list = name_sent.split()
single_sentence = ''.join(name_list)
print("Number of occurrences of the letter `a` is:", single_sentence.count('a'))