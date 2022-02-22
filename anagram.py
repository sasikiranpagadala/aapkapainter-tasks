string1 = input('Enter String 1: ')
string2 = input('Enter String 2: ')
if(sorted(string1)== sorted(string2)):
    print("The given two strings are anagrams.")
else:
    print("The given two strings aren't anagrams.") 