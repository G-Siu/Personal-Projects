import os

from pypdf import PdfMerger


pdfs = []
while True:
    file_name = input("Enter the pdf file name to be merged. Type 'Done' "
                      "once pdf files have been added:\n")
    if file_name.lower() == "done":
        if len(pdfs) < 2:
            print("Requires more than 1 pdf file to merge together.")
        else:
            break
    else:
        pdfs.append(file_name)

merger = PdfMerger()
for pdf in pdfs:
    merger.append(pdf)
combined_file = input("Enter the file name to be created including the pdf "
                      "extension:\n")
merger.write(combined_file)
merger.close()
os.startfile(combined_file)
