letter = input("Enter a word to check for its vowels and consonants: ").strip().upper()

vowels = "AEIOU "

vowel_counter = 0
consonant_counter = 0

for character in letter:
    if character in vowels:
        vowel_counter = vowel_counter+1
    else:
        consonant_counter = consonant_counter+1

print("Vowels:", vowel_counter)
print("Consonants:", consonant_counter)