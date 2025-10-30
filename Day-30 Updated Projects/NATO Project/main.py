import pandas
data = pandas.read_csv("Day-26 NATO Alphabet/nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
convert = True
while convert:
    user_choice = input("Enter the word(exit to stop): ")
    if user_choice.lower() == "exit":
        convert = False
    else:
        try:
            word_list = [data_dict[char.upper()] for char in user_choice if char != ' ' ]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
        else:
            print(word_list)