import functions
import math

with open('words.txt', 'r') as f:
    words = f.readlines()
i = 1
while i == 1 :
    spell = input()
    if spell == "quit":
        break

    suggestIndex = 0
    results = {}
    error = True

    for word in words:
        word = word.strip()
        ## the word is exist
        if spell == word:
            print("no error")
            error = False
            break
    if error:

        for word in words:
            word = word.strip()
            percentage =  math.ceil(functions.like(spell,word))
            if  percentage > 70:
                results[word] = percentage
    s = [(k, results[k]) for k in sorted(results, key=results.get, reverse=True)]
    for k, v in s:
        print(k)
