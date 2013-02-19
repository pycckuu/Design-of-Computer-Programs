# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    textCopy = text.lower()
    reversedText = str(text.lower())[::-1]
    # print len(textCopy)
    # print textCopy, reversedText
    i=0
    j=0
    for i in range(len(textCopy)):
        if str(textCopy[i:]) == str(textCopy)[i:][::-1]:
            return (i,len(textCopy)-i)
        if str(textCopy[j:]) == str(textCopy)[j:][::-1]:
            return (j,len(textCopy)-j)
        for j in range(len(reversedText)-i):
            if str(reversedText[j:]) == str(reversedText)[j:][::-1]:
                return (i,len(textCopy)-j)
            if textCopy[i:] == reversedText[j:]:# and len(textCopy[i:i-j])!=0 :
                print textCopy[i:i-j]
                print reversedText[j:j-i]
                print (i,len(textCopy)-j)
                return (i,len(textCopy)-j)

            #if 
    

    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'
test()
#longest_subpalindrome_slice('racecar')