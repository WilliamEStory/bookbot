def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_dict = count_chars(file_contents)
        formatted_dict = format_report(char_dict)

        print(f"--- Being report of {book} ---")
        print(f"Word count: {word_count}")
        for item in formatted_dict:
            print(f"'{item['char']}' was found: {item['count']} times")
        print(f"--- End of report ---")

def count_words(book_contents):
    words = book_contents.split()
    return len(words)

def count_chars(book_contents):
    char_dict = {}
    lower_case = book_contents.lower()
    for char in lower_case:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def format_report(char_dict):
    dict_list = []
    for char in char_dict:
        dict_list.append({
            "char": char,
            "count": char_dict[char]
        })
    
    dict_list.sort(key=lambda x: x["count"], reverse=True)
    return dict_list

main()