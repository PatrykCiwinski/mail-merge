#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as name_file:
    all_names=name_file.readlines()

#Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as starting_file:
    contents=starting_file.read()
    for name in all_names:
        stripped_name=name.strip()
        new_file=contents.replace("[name]", stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_file)
