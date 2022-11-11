#12. Get a string from an input string, where all occurance of first character replaced with '$' except first character
sentence = input("Enter a sentence:")
first_letter = sentence[0].lower()

sub_sec_half = ['$' if (x.lower() == first_letter) else x for x in sentence[1:]]
final_sent = first_letter + ''.join(sub_sec_half)
print(final_sent)