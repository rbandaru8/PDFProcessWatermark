import PyPDF2
import sys


#pdf merger - to merger multiple files. As this is accepting inputs, 
# we can run it as>python ImgProjects/PDfprocess.py dummy.pdf twopage.pdf wtr.pdf

inputs = sys.argv[1:]

def mergePdfs(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdffile in inputs:
        print(pdffile)
        merger.append(pdffile)
    merger.write('./pdfs/supermerger.pdf')

#call pdf merger
#mergePdfs(inputs)
