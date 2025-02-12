with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        clean_name = name.strip()
        new_letter = letter.replace("[name]", clean_name)
        with open(f"./Output/ReadyToSend/letter_for_{clean_name}.txt", "w") as invit_letter:
            invit_letter.write(new_letter)