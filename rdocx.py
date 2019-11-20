# using python-docx library
# pip install python-docx
from docx import Document

# we are loading only one page document file.
doc = Document("2.docx")
fulltext = []

# going paragraph by paragraph in one page
for para in doc.paragraphs:
    fulltext.append(para.text)

# print(fulltext)
print("\n")
print(fulltext[22:26])
# here you can see that we are getting null value for checkbox.
# searching on how to extract that checkbox or read image
