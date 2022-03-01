
def palindrome(word):
    """
    This function checks if the given argument is a palindrome.
    Argument: 
    word 
    Returns:
    boolean
    """
    print(word.lower() == word[::-1].lower())
  


my_word = input("Type in a word to check: ")

palindrome(my_word)
