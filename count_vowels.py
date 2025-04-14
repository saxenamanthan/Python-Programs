word = input("Enter the word - ")

word= word.lower()

ar_vowel = []
ar_consonant = []

for ch in word:
    #print(ch)
    if ch == 'a' or ch == 'e' or ch == 'i' or ch =='o' or ch == 'u':
        #print(ch)
        ar_vowel.append(ch)
    else:
        #print(ch)
        ar_consonant.append(ch)
        
print(f"Total number of vowel in the given string {word} is {len(ar_vowel)}")
print(f"Total number of consonants in the given string {word} is {len(ar_consonant)}")
    