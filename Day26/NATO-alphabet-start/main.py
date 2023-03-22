import pandas as pd
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pd.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(new_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the name : ").upper()
# print(user_input)
output_list = [new_dict[letter] for letter in user_input]
print(output_list)
