
def palindrome(word):
    """
    This function checks if the given argument is a palindrome.
    Argument: 
    word 
    Returns:
    boolean
    """
    return word.lower() == word[::-1].lower()
  


my_word = input("Type in a word to check: ")

print(palindrome(my_word))
