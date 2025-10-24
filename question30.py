word_list = input("Enter a list of words (comma-separated): ").split(',') 
long_len = 0 
long_word = "" 
for word in word_list: 
    word = word.strip() 
    curr_len = len(word) 
    if curr_len > long_len: 
        long_len = curr_len 
        long_word = word 
print(f"Longest word: '{long_word}' with length {long_len}")
