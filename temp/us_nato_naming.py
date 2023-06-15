import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
df = pd.DataFrame(nato_data)

#convert the df into a dictionary
nato_dict = {row.letter:row.code for (index,row) in df.iterrows()}
user_input = input("Please enter the code which you want to transmit")

result = [nato_dict[f"{string}"] for string in user_input.strip().upper() if string in nato_dict[f"{string}"] ]
print(result)