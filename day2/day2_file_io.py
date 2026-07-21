# day2_file_io.py
def file_io():
    input_path = "data/samples.txt"
    with open(input_path, "r") as file:
        text = file.read()
    print(text)
    lines = text.splitlines()
    line_count = len(lines)
    print("The text has",line_count,"lines")
    text = text.lower()
    text = text.replace(".","")
    text = text.replace(",","")
    words = text.split()
    word_count = len(words)
    print("Words:",words)
    print("The text has",word_count,"words")
    unique_word = set(words)
    unique_word_count = len(unique_word)
    print("The text has",unique_word_count,"unique words")
    word_frequency = {}
    for word in words :
        if word in word_frequency:
            word_frequency[word] = word_frequency[word] + 1
        else:
            word_frequency[word] = 1        
    print(word_frequency)
    top_10_words = sorted(word_frequency.items(),key = lambda item:item[1],reverse = True)[:10]
    print("Top 10 words:",top_10_words)
    output_path = "data/day2_file_summary.txt"
    with open(output_path,"w") as file:
        file.write(f"Line count:{line_count}\n")
        file.write(f"Word count:{word_count}\n")
        file.write(f"Unique word count:{unique_word_count}\n")
        for word, count in top_10_words:
            file.write(f"{word}: {count}\n")

if __name__ == "__main__":
    file_io()