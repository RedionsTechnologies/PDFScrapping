import PyPDF2
import tabula
from tabula import convert_into

def readPdf():
    try:
        pdfFileObj = open('demoData.pdf', 'rb')
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
def readTablePdf():
    try:
        # Tabula Information
        # print(tabula.environment_info())
        # df = tabula.read_pdf("11.pdf", output_format="json")
        # df = tabula.read_pdf("demoData.pdf", multiple_tables=True, pages='all')
        # df = tabula.read_pdf("11.pdf", multiple_tables=True)
        # in order to print first 5 lines of Table
        # print("Head of PDF", df.head())
        # print("JSON DATA: \n", df)

        ####### TO SAVE JSON INTO JSON FILE
        convert_into("demoData.pdf", "output.json", output_format="json", multiple_tables=True, pages='all')
    except Exception as ex:
        print("Exception in opening file: ", ex)

if __name__ == "__main__":
    readPdf()
    readTablePdf()