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
        i=7
        while not i==0:
            print("\n 1: Print DataFrame\n 2: Print JSON\n 3: Print Single Table\n 4: Print Multiple Tables ")
            print(" 5: Save to JSON File\n 6: Save to CSV File\n 7: Tabula Info\n 0: EXIT")
            i = int(input("Choose one of the options from above: "))
            if i == 1:
                df = tabula.read_pdf(fileName) # Simply reads pdf and returns in DataFrame format
                print("DATA: \n", df)
            elif i == 2:
                df = tabula.read_pdf(fileName, output_format="json") # Reads and returns data in Json format
                print("JSON DATA: \n", df)
            elif i == 3:
                df = tabula.read_pdf(fileName) # Returns first occurence of table - we can even specify page numbers to retreive table from
                print("SINGLE TABLE DATA: \n", df)
            elif i == 4:
                df = tabula.read_pdf(fileName, multiple_tables=True, pages="all") # Returns all tables data
                print("ALL TABLES DATA: \n", df)
            elif i == 5:
                ####### TO SAVE JSON INTO JSON FILE
                output = input("ENTER OUTPUT FILE NAME")
                # Reads and saves the complete file data in JSON format into an external JSON file of given name
                convert_into(fileName, output, output_format="json", multiple_tables=True, pages='all')
            elif i == 6:
                ####### TO SAVE JSON INTO CSV FILE
                output = input("ENTER OUTPUT FILE NAME")
                # Reads and saves the complete file data in CSV format into an external CSV file of given name
                convert_into(fileName, output, output_format="csv", multiple_tables=True, pages='all')
            elif i == 7:
                #Tabula Information
                print("TABULA INFORMATION:\n", tabula.environment_info())
            else:
                break

    except Exception as ex:
        print("Exception in opening file: ", ex)

if __name__ == "__main__":
    # Enter filename to be used here - we have used 2 libraries here to extract data - pypdf2 and tabula
    # At the moment only tabula seems to be working as required
    fileName = "demoData.pdf" #input("ENTER FILENAME: ")
    # ------ METHOD 1 ------ #
    # readPdf(fileName)
    # ------ METHOD 2 ------ #
    readTablePdf(fileName)