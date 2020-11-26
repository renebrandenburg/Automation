import PyPDF2
import os 

pdfFile = open('example.pdf', 'rb')
pdfFile2 = open('example2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdfFile)
reader2 = PyPDF2.PdfFileReader(pdfFile2)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdfFile.close()
pdfFile2.close()