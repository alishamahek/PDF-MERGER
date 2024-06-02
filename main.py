from pypdf import PdfMerger

pdfs = ["html1.pdf", "html2.pdf", "html3.pdf", "html4.pdf", "html5.pdf", "html6.pdf"]
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)
merger.write("Result.PDF")
merger.close()