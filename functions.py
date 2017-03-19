import char_check

def check_indexed(word1,word2):
    occur = 0
    new_occur = 0
    counter1 = 0
    counter2 = 0

    ## arithmetic
    x = (len(word1) + len(word2)) / 2

    ## loop to compare letters of words
    while counter1 < len(word1) and counter2 < len(word2):
        ## the same letters
        if word2[counter2] == word1[counter1]:
            occur += 1
        ## if the letters not the same
        else :
            ## break if the counter at the last letter
            if counter2 == len(word2) - 1:
                break
            ## loop for step i letter from word 2
            for i in range(1,3):
                ## break to avoid out index i+counter > last index
                if counter2 + i == len(word2) - 1:
                    break
                ## if letter of word2 after add i identical with letter of word1
                if word2[counter2+i] == word1[counter1]:
                    new_occur +=1
                    counter2 = counter2 + i -1
                    break
            ## if the the percentage still small check the identical of words by changing
            ## the index of word1
            if  (occur+new_occur/x)*100 < 70:
                new_occur = 0
                ## loop for step i letter from word 1
                for m in range(1,3):
                    ## break to avoid out index i+counter > last index
                    if counter1+m > len(word1) -1:
                        break
                    ## if letter of word1 after add i identical with letter of word2
                    if word2[counter2] == word1[counter1+m]:
                        new_occur += 1
                        counter1 = counter1 + i - 1

        counter1 += 1
        counter2 += 1
    ## get the overall identical times
    occur = occur + new_occur
    if occur != 0:
        x = (len(word1) + len(word2) )/ 2
        percentage = (occur/x)*100
        return percentage
    else:
        return 0

def like(word1, word2):

    percentage = check_indexed(word1, word2) + char_check.check_chars(word1,word2)

    if percentage > 50:
        return percentage

    else:

        if word1 in word2:
            percentage = (len(word1)/len(word2))*100
            return percentage
    return 0
