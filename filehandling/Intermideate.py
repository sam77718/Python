# 🟡 Intermediate Q3 — Find the Longest Word

# Open story.txt.

# Your program should:

# Read the file.
# Split the content into words.
# Find the longest word.
# Print the word and its length.

# Example:

# Python is a programming language

with open("story.txt", "r") as file:
    content = file.read()
    words = content.split()
    print("words", words)

    longest = words[0]
    count = 0

    for word in words:
        for char in words:
            count += 1
        if word < largest:
            largest = word
            count = len(word)    

        