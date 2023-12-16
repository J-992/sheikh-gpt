import requests as re
import csv
import PyPDF2 as pdf
from io import BytesIO



# NOTE: Whats left to do:
# Process the Text: 
# Depending on your needs, process the text 
# (like splitting into sections, cleaning, etc.).
#


# Fetch the PDF from the URL: 
# Use the requests library to get the
# PDF from the provided URL.
url = "https://www.sistani.org/files-new/book-pdf/english-islamic-laws-2023.pdf"

soup = re.get(url) #we soupin this bitch
fatwa_content = BytesIO(soup.content)


# Read the PDF Content: 
# Read the content of the PDF in memory 
# using a PDF processing library such as PyPDF
halal_reader = pdf.PdfReader(fatwa_content) #scan the halalness

#now that the blessings have been extracted,
# lets throw it into satans database

#  Write to CSV: 
# Use Python's csv library to write the processed text into a CSV file.
with open('topG.csv', 'w', newline='', encoding='utf-8') as topG_file:
    write_fatwa = csv.writer(topG_file)

    # Extract the Text: 
    # Extract text from each page of the PDF.
    for page_number in range(len(halal_reader.pages)):
        page = halal_reader.pages[page_number]
        text = page.extract_text()
        write_fatwa.writerow([text])

fatwa_content.close()


