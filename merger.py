import sys 
import PyPDF2

inputs=sys.argv[2:]

def pdf_combined(pdf_list):
	merger=PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write(sys.argv[1])
pdf_combined(inputs)