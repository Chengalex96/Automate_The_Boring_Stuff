# COmbine 2 pdfs together

import PyPDF2

# Read binary mode
pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfReader(pdfFile)

print(len(reader.pages))

page = reader.pages[0]
print(page.extract_text())

for pageNum in range (len(reader.pages)):
    page = reader.pages[pageNum]
    print(page.extract_text())

# Can only add or remove pages on pds, cannot change text or color

# Combine pdfs

import PyPDF2

pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfReader(pdf1File)
reader2 = PyPDF2.PdfReader(pdf2File)

writer = PyPDF2.PdfWriter()

for pageNum in range(len(reader1.pages)):
    page = reader1.pages[pageNum]
    writer.add_page(page)

for pageNum in range(len(reader2.pages)):
    page = reader2.pages[pageNum]
    writer.add_page(page)

# Write binary mode for pdf
outputFile = open('combinedMinutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()