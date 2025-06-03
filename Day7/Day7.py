filename = "/Users/hchethankumar/Desktop/python_workspace/Day7/sample.txt"  
with open(filename, 'r') as file:  
    content = file.read()
words = content.lower().split()  
word_count = {}
for word in words:
    clean_word = word.strip('.,!?;:"()')
    if clean_word:  
        if clean_word in word_count:
            word_count[clean_word] += 1
        else:
            word_count[clean_word] = 1

print("Word Count Results:")
for word, count in sorted(word_count.items()):
    print(f"{word}: {count}")