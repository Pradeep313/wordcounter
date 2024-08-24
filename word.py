def word_split(text):
    words = text.split()
    return words


def word_counter(words):
    word_count = len(words)
    return word_count


def main():
    # here take input from the user
    text = input(" enter a sentence or paragraph: ")

    # here sentence or paragraph split
    word_splitting = word_split(text)

    # here count word
    word_counts = word_counter(word_splitting)

    # here print number of word
    print(f"The number of words in the text is: {word_counts}")


if __name__ == "__main__":
    main()
