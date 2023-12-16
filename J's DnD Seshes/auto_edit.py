# Auto editor for DnD README.md
# Date created: 15th Dec 2023
# Date modified: 15th Dec 2023
# Name: G Siu

# Names changed to specified colour for ease of reading

# Open README_edit.md and convert with specified changes
with open("README_edit.md", "r") as infile, open("README.md", "w") as outfile:
    # Names to be replaced for coloured version
    replacements = {"Jessy": '<span style="color:#46503C">Jessy</span>',
                    "Pip": '<span style="color:#6C5078">Pip</span>',
                    "Renfri": '<span style="color:#141524">Renfri</span>',
                    "Lia": '<span style="color:#BAE8FF">Lia</span>'
                    }

    # Convert player names to colour version
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)

