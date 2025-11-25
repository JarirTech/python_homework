
def pig_latin(word):
    vowel =["a", "e", "i", "o", "u"]
    

    for i, char in enumerate(word):
        if i==0 and char in vowel:
            result =word+"ay"
    #print(result)
        elif i == 0 and char not in vowel:
             result = word[1:]+ word[i]+ "ay" #  -> bananabay
        elif i==1 and char not in vowel:
            result = word[2:]+ word[0]+word[1]+"ay" #cherry == errychay
        elif word.startswith("qu"):
            
            result = word[2:]+"qu"+"ay" # "quiet") == "ietquay"
        elif  word[i] =="q" and word[i+1] == "u":# "square") == "aresquay"
            cluster = word[i:i+2] 
            new_word = word[:i] + word[i+2:]  # remove "qu"
            result = new_word + cluster + "ay"
       

    print(result)
    return result

pig_latin("square") 
# ("banana") == "ananabay"

# ("quiet") == "ietquay"
# ("square") == "aresquay"
# ("the quick brown fox") == "ethay ickquay ownbray oxfay