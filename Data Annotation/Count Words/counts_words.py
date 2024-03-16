def count_word_occurrences(file_path):
    word_counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()  # Convert to lowercase to make the comparison case-insensitive
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}: {count}")


count_word_occurrences("input.txt")
# Need to strip punctuation
