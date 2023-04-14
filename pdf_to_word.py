import PyPDF2 
myFile = open("input.pdf","rb")
output_file = open("output.docx", "w")
reader = PyPDF2.PdfReader(myFile)
numOfPages = len(reader.pages)
for i in range(numOfPages):
    page = reader.pages[i]
    text = page.extract_text()
    output_file.write(text)
output_file.close()
myFile.close()

