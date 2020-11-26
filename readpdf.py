import PyPDF2
import os 

pdfFile = open('example.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)

reader.numPages

page = reader.getPage(0)
page.extractText()

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())