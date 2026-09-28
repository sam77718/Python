# Create a new file called unique_words.txt containing each word only once.

# Example story.txt:

# Python is easy Python is powerful Python

# unique_words.txt should contain:

# Python
# is
# easy
# powerful

with open('story.txt','r') as file:
    content =file.read()
    words = content.split()
    print("stoty file words", words)

    

with open('unique_words.txt','w') as file:
    lst = []
    for word in words:
        if word in lst:
            continue
        else:
            lst.append(word)

    for word in lst:
        file.write(word + '\n')


