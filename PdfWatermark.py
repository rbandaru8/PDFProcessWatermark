import PyPDF2
import sys

#watermarks all the files. 

def watermark_files(pdf_file, watermark_file, output_file):
        input_pdf = PyPDF2.PdfReader(open(pdf_file,'rb'))
        watermark_pdf = PyPDF2.PdfReader(open(watermark_file,'rb'))
        watermark_page = watermark_pdf.pages[0]

        output = PyPDF2.PdfWriter()
        for i in range(len(input_pdf.pages)):
            page = input_pdf.pages[i]
            page.merge_page(watermark_page)
            output.add_page(page)

        with open(output_file,'wb') as watermarkedfile:
            output.write(watermarkedfile)

#call watermark function
watermark_files('./pdfs/supermerger.pdf','./pdfs/wtr.pdf','./pdfs/watermarked.pdf')

