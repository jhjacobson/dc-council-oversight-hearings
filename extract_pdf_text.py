import pdfplumber
import re

def extract_and_write_text_from_pdf(pdf_path):
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text()
    
    return full_text

pdf_path = 'schedule.pdf'
full_text = extract_and_write_text_from_pdf(pdf_path)

with open('schedule_pdf_as_text.txt', 'w', encoding='utf-8') as file:
    file.write(full_text)
