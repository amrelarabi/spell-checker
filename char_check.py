def check_chars(word1,word2):
    i = 0
    j = 0
    occur = 0
    while i < len(word1) and j < len(word2):
        if word1[i] in word2:
            occur+=1
        i+=1
        j+=1
    chars_percentage = occur/((len(word1)+len(word2))/2)
    return  chars_percentage
