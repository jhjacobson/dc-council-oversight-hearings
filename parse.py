import pdfplumber
import re

def extract_hearings_from_pdf(pdf_path):
    hearings = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            pattern = r'COMMITTEE ON (.+?) Chairperson .+?\n(.+?); .+?\nTime Agency(?: \(.*?\))?\n(.+? a\.m\.|p\.m\.) - (.+? a\.m\.|p\.m\.) (.*?)(?:\nThis hearing|\nCOMMITTEE|$)'
            matches = re.findall(pattern, text, re.DOTALL)
            for match in matches:
                hearing_info = {
                    "committee": match[0].strip(),
                    "date": match[1].strip(),
                    "time": f"{match[2].strip()} - {match[3].strip()}",
                    "agencies": match[4].replace("\n", " ").strip()
                }
                hearings.append(hearing_info)

    return hearings

def create_html(hearings):
    html = "<html><head><title>Hearing Schedule</title></head><body>"
    html += "<h1>Council of the District of Columbia - Public Hearings Schedule</h1>"
    html += "<table border='1'><tr><th>Committee</th><th>Date</th><th>Time</th><th>Agencies</th></tr>"

    for hearing in hearings:
        html += f"<tr><td>{hearing['committee']}</td><td>{hearing['date']}</td><td>{hearing['time']}</td><td>{hearing['agencies']}</td></tr>"

    html += "</table></body></html>"
    return html

pdf_path = 'schedule.pdf'

hearings = extract_hearings_from_pdf(pdf_path)
html_output = create_html(hearings)

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_output)


