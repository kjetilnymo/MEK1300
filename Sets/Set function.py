
def main():
    sentence = input("Enter a sentence: ")

    unique_words = set()
    
    words = sentence.split()

    for word in words:
        cleaned = clean(word)
        if cleaned != "":
            unique_words.add(cleaned)

    print("The sentence obtains:", len(unique_words), "unique words")


def clean(string):
    result = ""
    for char in string:
        if char.isalnum():
            result = result + char.lower()

    return result

main()