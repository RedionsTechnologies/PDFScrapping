"""
this file will parse data form pdf
And output will be into json or csv
"""
# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument
import tabula


# def get_metadata_info(path):
#     file = open(path, 'rb')
#     parser = PDFParser(file)
#     doc = PDFDocument(parser)
#
#     return doc.info


def extract_table(path):
    """
    Extracting table from sample pdf into csv
    :param path: pdf file from directory
    :return: saves data into csv and json file
    Error: It saves data as expect checkbox column
            Does not get Column names correctly.
    """
    directory = "output_data"
    filename = path.split("/")[-1]
    filename = filename.split(".")[0]
    df = tabula.read_pdf(path)
    df.to_csv(directory+"/"+filename+".csv")
    df.to_json(directory+"/"+filename+".json")


def get_pdf_data():
    pass


def main():
    extract_table("input_data/11.pdf")


if __name__ == '__main__':
    main()
