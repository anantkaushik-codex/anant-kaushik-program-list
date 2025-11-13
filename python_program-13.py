s = input("Enter string: ")
count = sum(1 for i in s.lower() if i in "aeiou")
print("Vowels:", count)