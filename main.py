def main():

    book_path = "books/Frankenstein.txt"
    print(f"*** Word and Letter count of {book_path} ***")
    text = book_read(book_path)
    words = word_count(text)
    print(f"            This book contains {len(words)} words")
    print("")
    letters = letter_count(words)
    list_of_dictionaries = dictionary_to_list(letters)
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    for items in list_of_dictionaries:
        print(f"            The letter {items["letter"]} appears {items["num"]} times")
    print("")
    print("                 *** End of Report ***")

def sort_on(letters):
    return letters["num"]

def dictionary_to_list(letters):
    letter_list = []
    for letter in letters:
        current_dictionary = {
            "letter": letter,
            "num" : letters[letter]        
            }
        letter_list.append(current_dictionary)
    return letter_list

def letter_count(words):
    joined = "".join(words)
    lower_case = joined.lower()
    letter_dictionary = {}
    for letter in lower_case:
        if letter.isalpha() and letter in letter_dictionary:
            letter_dictionary[letter] += 1
        elif letter.isalpha():
            letter_dictionary[letter] = 1
    return letter_dictionary

def word_count(text):
    return text.split()

def book_read(book_path):
    with open(book_path) as f:
        return f.read()

main()


