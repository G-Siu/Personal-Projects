def decode(message_file):
    # Format input file into dictionary
    message_list = message_file.splitlines()
    # Sort the list in ascending order from 1-6
    message_list.sort()
    # Staircase function outputs
    # [['1 I'], ['2 dogs', '3 love'], ['4 cats', '5 you', '6 computers']]
    step = 1
    pyramid = []
    while len(message_list) != 0:
        if len(message_list) >= step:
            pyramid.append(message_list[0:step])
            message_list = message_list[step:]
            step += 1
        else:
            return False
    # Get last word in each row of pyramid and append to list
    get_words = [row[-1].split()[1] for row in pyramid]
    # Join words to form sentence as string
    decoded_message = " ".join(get_words)
    return decoded_message


# Open txt file with the encoded message
with open("message.txt", "r") as f:
    file = f.read()

print(decode(file))
