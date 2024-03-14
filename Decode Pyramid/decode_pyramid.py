def decode(message_file):
    # Format input file into dictionary
    message_list = message_file.splitlines()
    return message_list


with open("message.txt", "r") as f:
    file = f.read()

print(decode(file))
