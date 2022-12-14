def is_palidrom(word):
    reversed_word=word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
    # at palce of 5 and 6
    #return False is also correct
print(is_palidrom("naman"))
print(is_palidrom("horse"))