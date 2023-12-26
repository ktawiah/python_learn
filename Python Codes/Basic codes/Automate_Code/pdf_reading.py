from pathlib import Path
import PyPDF2

pdf_path = Path(
    "100 Days of code miscellaneous/12+Rules+to+Learn+to+Code+[2nd+Edition]+2022.pdf"
)

with open(pdf_path, "r", encoding="UTF-8"):
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    print(pdf_reader.numPages)
    print(pdf_reader.getPage(1).extract_text())
