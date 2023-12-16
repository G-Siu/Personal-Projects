# Auto editor for DnD README.md
# Date created: 15th Dec 2023
# Date modified: 15th Dec 2023
# Name: G Siu

# Names changed to specified colour for ease of reading

# Open README.md file
with open("README.md", "r") as f:
    # lines = f.readlines()

    replacements = {"Jessy": '<span style="color:#46503C">Jessy</span>',
                    "Pip": '<span style="color:#6C5078">Pip</span>'}

    # Convert player names to colour version
    text = []
    for line in f:
        if (line.find("Jessy") is not False and
                line.find('<span style="color:#46503C">Jessy</span>') == -1):
            for src, target in replacements.items():
                text.append(line.replace(src, target))
# for line in text:
#     if (line.find("Pip") is not False and
#             line.find('<span style="color:#6C5078">Pip</span>') == -1):
#         for src, target in replacements.items():
#             text.append(line.replace(src, target))

for line in text:
    print(line)
