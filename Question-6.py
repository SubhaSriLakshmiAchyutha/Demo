sentence = "I am a teacher and I love to inspire and teach people"
list = sentence.split(' ')          #Split function by default uses whiteSpaces as the separator in the string sentence
print(list)
unique_words=len(set(list))                #number of unique words in given string
print(f"number of unique words in the given string: ",unique_words )      # printing the Unique_words length

