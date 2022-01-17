def isPalindrome(word):
    word = word.lower()
    word_length = len(word)

    if word_length < 2:
        return True
    
    elif word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    
    else:
        return False



'''Manuel Tests'''

# print(isPalindrome('word'))
# print(isPalindrome('abba'))
# print(isPalindrome('aaaabbcdbbaaaa'))
