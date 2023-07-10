import PyPDF2
import sys


#function to rotate pdffile with rotatedegrees and output to outfile.
def pdfrotate(pdffile, rotatedegrees, outfile):
    with open(pdffile,'rb') as file:
        reader = PyPDF2.PdfReader(file)
        getpagecount = len(reader.pages)
        page = reader.pages[0]
        page.rotate(rotatedegrees)
    
        writer = PyPDF2.PdfWriter()
        writer.add_page(page)
    with open(outfile,'wb') as new_file:
        writer.write(new_file)

#Call functions
#pdfrotate('./pdfs/dummy.pdf',180,'./pdfs/dummyclockwise.pdf')

