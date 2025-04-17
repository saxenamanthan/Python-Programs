sentence = input("Enter the sentence - ")
vowels = "aeiou"

array_consonants = [ch for ch in sentence.lower().replace(" ","") if ch not in vowels]
array_vowels = [ch for ch in sentence.lower().replace(" ","") if ch in vowels]


print(f"The no of consonants in a sentence is {len(array_consonants)}")
print(f"The no of vowels in a sentence is {len(array_vowels)}")


 

