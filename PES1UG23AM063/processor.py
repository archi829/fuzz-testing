def sanitize_string(data):
    """
    Removes special characters and trims the input.
    Assumes data is a non-empty string.
    """
    if data is None:
        return ""
    
    data = data.strip()
    for ch in ['!', '@', '#', '$', '%']:
        data = data.replace(ch, '')
    return data

def parse_int_list(csv_string):
    """
    Parses a CSV string of integers into a list of ints.
    Assumes valid comma-separated integer input.
    """
    if csv_string is None:
        return []
    parts = csv_string.split(',')
    
    nums = []
    for p in parts:
        if p: # This skips empty strings like ''
            try:
                nums.append(int(p))
            except ValueError:
                continue
    return nums

def reverse_words(sentence):
    """
    Reverses each word in a sentence.
    Assumes sentence is non-empty and contains no punctuation.
    """
    if sentence is None:
        return ""
    words = sentence.split()
    reversed_words = [w[::-1] for w in words]
    return ' '.join(reversed_words)

def main():
    print("==== Running sanitize_string ====")
    raw_string = input("Enter a string with special characters (!,@,#,$,%): ")
    clean_string = sanitize_string(raw_string)
    print("Sanitized String:", clean_string)

    print("\n==== Running parse_int_list ====")
    csv_input = input("Enter a CSV of integers (e.g. 1,2,3,4): ")
    int_list = parse_int_list(csv_input)
    print("Parsed Integer List:", int_list)

    print("\n==== Running reverse_words ====")
    sentence_input = input("Enter a sentence without punctuation: ")
    reversed_sentence = reverse_words(sentence_input)
    print("Reversed Words Sentence:", reversed_sentence)

if __name__ == "__main__":
    main()
