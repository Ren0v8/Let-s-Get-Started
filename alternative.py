# store string in variable called "sentence"
# create empty string called "final_sentence" to store the result
# split the sentence and store in variable called "words"
sentence = "hickory dickory dock, the mouse ran up the clock"
final_sentence = ""
words = sentence.split()

# Step 1:

# create for loop
#   if the index values are divisible by 2:
#       every second index value is in uppercase
#   else:
#       every other index value is in lowercase
# print(final_sentence)
for i in range(len(sentence)):

    if i % 2 == 1:
        
        final_sentence += sentence[i].upper()

    else:
        final_sentence += sentence[i].lower()

print(final_sentence)


# Step 2:
# create for loop
#   if the index values are divisible by 2:
#       print(every second indexed word is in uppercase)
#   else:
#       print(every other indexed word is in lowercase)
# print(final_sentence)
for i in range(len(words)):
    
    if i % 2 == 0:
        print(words[i].lower(), end=" ")

    else:
        print(words[i].upper(), end=" ")

