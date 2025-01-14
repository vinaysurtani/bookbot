def count_words(str):
    words = str.split()
    count = 0
    for word in words:
        count += 1
    return count


def count_chars(str):
    char_dict = {}
    for c in str:
        c = c.lower()
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    return char_dict

def main():
    with open("books/frankenstein.txt") as f:
        print("--- Begin report of books/frankenstein.txt ---")
        file_contents = f.read()
        words = count_words(file_contents)
        charset = count_chars(file_contents)
        sorted_chars = sorted(charset.items(),key=lambda item: item[1], reverse=True)
        sorted_charlist = [c for c in sorted_chars if c[0].isalpha()]
        print(f"{words} words found in the document")
        print()
        for i in sorted_charlist:
            print(f"The '{i[0]}' character was found {i[1]} times")
        print("--- End report ---")

main()