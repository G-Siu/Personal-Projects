def decode(message_file):
    # Format input file into dictionary
    message_list = message_file.splitlines()
    # Split the number from word in each value in list and append to new list
    split_list = [word.split() for word in message_list]
    # Convert number values in each list into integer
    sort_list = [[int(num), word] for num, word in split_list]
    # Sort by the number value
    sort_list.sort(key=lambda num: (num[0]))
    # Staircase function outputs
    # [['1 I'], ['2 dogs', '3 love'], ['4 cats', '5 you', '6 computers']]
    step = 1
    pyramid = []
    while len(sort_list) != 0:
        if len(sort_list) >= step:
            pyramid.append(sort_list[0:step])
            sort_list = sort_list[step:]
            step += 1
        else:
            return False
    # Get last word in each row of pyramid and append to list
    get_words = [row[-1][1] for row in pyramid]
    # Join words to form sentence as string
    decoded_message = " ".join(get_words)
    return decoded_message


# Open txt file with the encoded message
with open("coding_qual_input.txt", "r") as f:
    file = f.read()

print(decode(file))
