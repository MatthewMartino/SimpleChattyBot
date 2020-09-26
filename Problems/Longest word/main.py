word1 = input()
word2 = input()

temp_array1 = []
temp_array2 = []

# How many letters does the longest word contain?

for letter in word1:
    temp_array1.append(letter)

for letter in word2:
    temp_array2.append(letter)

if len(temp_array1) > len(temp_array2):
    print(len(temp_array1))
else:
    print(len(temp_array2))
