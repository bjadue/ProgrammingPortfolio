# Brandon Jadue
# 11/29/23
# Program will reverse a string provided by user

def reverse_words_and_chars(sentence):
    revStr = ''
    straList = []
    for i in range(int(len(sentence)), 0, -1):
        # print(input[i-1], end=" ")
        # print(i-1)
        straList.append(sentence[i-1])
    for char in straList:
        revStr += char
    return revStr

usrInput = str(input("Enter a sentence to reverse its words and characters: "))

revInput = reverse_words_and_chars(usrInput)
print(f"Reversed Sentence: {revInput}")
