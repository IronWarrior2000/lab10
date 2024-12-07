#Bill Nguyen | 12/5/24 | Lab 10


def isPalindromes(palindromes, left, right): 
    if left >= right: #If the left character is more than or equal to the right character it will return true.
        return True
    
    while left < right and not palindromes[left].isalnum(): #Checks if the letter is not the same or has numbers to the left
        left += 1
    while left < right and not palindromes[right].isalnum(): #Checks if the letter is not the same or has numbers to the right
        right -= 1
    
    if palindromes[left].lower() != palindromes[right].lower(): #if both sides does not match then it will return False
        return False
    
    return isPalindromes(palindromes, left + 1, right - 1) #This repeat itself until the string is empty

def countVowel_Consonant(word, index = 0, vowels = 0, consonants = 0):
    if index == len(word): #If index is the same as the total length of word then it will return vowels and consonants
        return vowels, consonants
    
    char = word[index].lower() #char is equal to the lowered word of an index
    if char in "aeiou": #if char has AEIOU in it then it will count vowels
        return countVowel_Consonant(word, index + 1, vowels + 1, consonants) 
    elif char in "bcdfghjklmnpqrstvwxyz": #if char has any consonants then it will count consonants
        return countVowel_Consonant(word, index + 1, vowels, consonants + 1)
    else: #else it will not count if the string has numbers, special characters, and more.
        return countVowel_Consonant(word, index + 1, vowels, consonants)

def main():
    
    palindromes = input("Enter in a string") #The user will enter in the string here
    isPalindromes(palindromes, 0 , len(palindromes) - 1) #This will check if the string is a palindrome or not
    vowels, consonants = countVowel_Consonant(palindromes)  #This is to record the total amount of vowels and consonants
    #This will print out the total data value.
    print(f"Is {palindromes} a palindrome? {'Yes' if isPalindromes else 'No'} \nTotal Vowels : {vowels} \nTotal Consonants : {consonants}")
    if vowels > consonants:
        print("There are more vowels than consonants")
    else:
        print("There are more consonants than vowels")
        
main()