import PyPDF2
import tabula
from pandas import DataFrame

try:
    pdfFileObj = open('sample.pdf', 'rb')
    print("FILE OPENED with Object :", pdfFileObj)
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    if pdfReader.isEncrypted:
        print("ENCRYPTED")
        pdfReader = pdfReader.decrypt("ENTER PASSWORD HERE")
    print("Number of pages: ", pdfReader.numPages)
    for i in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        print("PDF Data: ", pageObj.extractText())
    pdfFileObj.close()
except Exception as ex:
    print("Exception in opening file: ", ex)

#FOR READING TABLE DATA
try:
    # Tabula Information
    # print(tabula.environment_info())
    df = tabula.read_pdf("demoData2.pdf")
    # in order to print first 5 lines of Table
    # print("Head of PDF", df.head())
    # df = tabula.read_pdf("demoData2.pdf", multiple_tables = True)
    # tabula.read_pdf("demoData2.pdf", area=(126, 149, 212, 462), pages=1)
    # tabula.read_pdf("demoData2.pdf", output_format="json")
except Exception as ex:
    print("Exception in opening file: ", ex)