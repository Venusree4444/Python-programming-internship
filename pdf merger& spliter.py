from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os

def merge_pdfs(input_paths, output_path):
    merger = PdfMerger()
    for path in input_paths:
        merger.append(path)
    merger.write(output_path)
    merger.close()
    print("PDFs merged successfully!")

def split_pdf(input_path):
    input_pdf = PdfReader(open(input_path, "rb"))
    input_filename = os.path.splitext(os.path.basename(input_path))[0]

    for i in range(len(input_pdf.pages)):
        output_pdf = PdfWriter()
        output_pdf.add_page(input_pdf.pages[i])
        output_path = f"{input_filename}page{i+1}.pdf"
        with open(output_path, "wb") as output_file:
            output_pdf.write(output_file)
        print(f"Page {i+1} extracted successfully to {output_path}")

# Example usage:
# Merge PDFs
input_files = ["pdf1.pdf", "pdf2.pdf", "pdf3.pdf"]
merge_pdfs(input_files, "merged.pdf")

# Split PDF
split_pdf("input.pdf")