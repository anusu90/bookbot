def count_characters(content):
    charMap = {}
    for char in content:
        formattedChar = char.lower()
        if formattedChar in charMap:
            charMap[formattedChar] += 1
        else:
            charMap[formattedChar] = 1

    return charMap

def count_words(content):
    words = content.split()
    return len(words)

def main():
    with open('./books/frankenstein.txt', 'r') as file:
        content = file.read()
        words = count_words(content)
        chars = count_characters(content)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        print("\n")
        for x in chars:
            print(f"The '{x}' character was found {chars[x]} times")
        
        print("--- End report ---")


if __name__ == '__main__':
    main()