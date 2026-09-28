# Read story.txt and count how many times each word appears.

# Then create:

# word_frequency.txt

# Example story.txt:

# Python is easy
# Python is powerful
# Python is popular
with open('story.txt', 'r') as file:
    content = file.read()
    words = content.split()

    freq = {}

    for word in words:
        word = word.lower()

        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    print(freq)

    with open('word_frequency.txt', 'w') as file:

        for word, count in freq.items():
            file.write(f"{word}: {count}\n")
        