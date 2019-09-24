import PyPDF2
import tabula
from tabula import convert_into

def readPdf(fileName = "demoData.pdf"):
    try:
        pdfFileObj = open(fileName, 'rb')
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
def readTablePdf(fileName = "demoData.pdf"):
    try:
        i=1
        while i>0 or i<0:
            print("\n 1: Print DataFrame\n 2: Print JSON\n 3: Print Single Table\n 4: Print Multiple Tables ")
            print(" 5: Save to JSON File\n 6: Save to CSV File\n 7: Tabula Info")
            i = int(input("Choose one of the options from above: "))
            if i == 1:
                df = tabula.read_pdf(fileName)
                print("JSON DATA: \n", df)
            elif i == 2:
                df = tabula.read_pdf(fileName, output_format="json")
                print("JSON DATA: \n", df)
            elif i == 3:
                df = tabula.read_pdf(fileName)
                print("JSON DATA: \n", df)
            elif i == 4:
                df = tabula.read_pdf(fileName, multiple_tables=True, pages="all")
                print("JSON DATA: \n", df)
            elif i == 5:
                ####### TO SAVE JSON INTO JSON FILE
                output = input("ENTER OUTPUT FILE NAME")
                convert_into(fileName, output, output_format="json", multiple_tables=True, pages='all')
            elif i == 6:
                ####### TO SAVE JSON INTO CSV FILE
                output = input("ENTER OUTPUT FILE NAME")
                convert_into(fileName, output, output_format="csv", multiple_tables=True, pages='all')
            elif i == 7:
                #Tabula Information
                print("TABULA INFORMATION:\n", tabula.environment_info())
            else:
                break

    except Exception as ex:
        print("Exception in opening file: ", ex)

if __name__ == "__main__":
    fileName = "demoData.pdf" #input("ENTER FILENAME: ")
    # readPdf(fileName)
    readTablePdf(fileName)