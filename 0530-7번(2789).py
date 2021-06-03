word=input()
pro=['C','A','M','B','R','I','D','G','E']

for i in range(len(word)):
    if word[i] in pro:
        word=word.replace(word[i], '_')
word=word.replace('_', '')
print(word)