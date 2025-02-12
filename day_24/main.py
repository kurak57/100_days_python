#TODO: Create a letter using starting_letter.txt 


names = open("./Input/Names/invited_names.txt", "r")
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names.readlines():
        clean_name = name.strip()
        new_letter = letter.replace("[name]", clean_name)
        with open(f"./Output/ReadyToSend/letter_for_{clean_name}.txt", "w") as file:
            file.write(new_letter)

names.close()
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp