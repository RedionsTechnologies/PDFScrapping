# PYTHON CODE START HERE

import PyPDF2

pdfFileObj = open('demoData.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

print(pageObj.extractText())