# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {}
for (index, row) in df.iterrows():
    letter = row.letter
    code = row.code
    nato_dict[letter] = code


while True:
    try:
        word = input("Enter a word: ").upper()
        phonetic_list = [nato_dict[letter] for letter in word]
        break
    except KeyError:
        print("Sorry, only letter in the alphabet please.")

print(phonetic_list)

