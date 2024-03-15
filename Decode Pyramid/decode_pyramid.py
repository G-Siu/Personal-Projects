def decode(message_file):
    # Format input file into dictionary
    message_list = message_file.splitlines()
    # Sort the list in ascending order from 1-6
    message_list.sort()
    # Staircase function outputs
    # [['1 I'], ['2 dogs', '3 love'], ['4 cats', '5 you', '6 computers']]
    step = 1
    subsets = []
    while len(message_list) != 0:
        if len(message_list) >= step:
            subsets.append(message_list[0:step])
            message_list = message_list[step:]
            step += 1
        else:
            return False
    return subsets


with open("message.txt", "r") as f:
    file = f.read()

print(decode(file))
