def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_word_count(text)
    lowercase = text.lower()
    letters = letter_count(lowercase)
    listed = listed_dict(letters)
    listed.sort(reverse=True, key=sort_on)
    sorted = listed
    new_list = storted_dict(sorted)
    report(new_list)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print(report(new_list))
    print("--- End report ---")   

def letter_count(lowercase):
    count = {}
    for char in lowercase:
        if char.isalpha():
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    return count


def sort_on(letters):
    return letters["num"]

def listed_dict(letters):
    list = [{"char": a, "num": b} for a, b in letters.items()]
    return list

def sort_on(listed):
    return listed["num"]    


def get_word_count(text):
    words = text.split()
    return len(words)


def get_text(path):
    with open(path) as f:
        return f.read()

def storted_dict(sorted): 
        new = {d["char"]: d["num"] for d in sorted}
        return new

def report(new_list):
    return "\n".join(f"The '{key}' character was found {str(value)} times" for key, value in new_list.items())
    

if __name__ == "__main__":
    main()