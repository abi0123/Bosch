with open("datafile.txt","r") as file:
    text= file.read()
words = text.split()
num_words = len(words)
print(num_words)

