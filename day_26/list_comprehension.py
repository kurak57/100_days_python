# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = "Tomi"
# word_name = [letter for letter in name]
# print(word_name)

# double_list = [n*2 for n in range(1,5)]
# print(double_list)

# odd_numbers = [num for num in range(1,10) if num%2 !=0]
# print(odd_numbers)

# names = ['Alex', 'Beth', 'Caroline','Dave', 'Eleanor','Freddie']

# up_name = [name.upper() for name in names if len(name) > 4]
# print(up_name)

with open("file1.txt") as file1:
    numbers1 = [int(n.strip()) for n in file1]
    
with open("file2.txt") as file2:
    numbers2 = [int(n.strip()) for n in file2]

print(numbers1)
print(numbers2)

result = [num for num in numbers1 if num in numbers2]

print(result)