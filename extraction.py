from typing import Union
from os.path import exists
import requests
from PyPDF2 import PdfReader

'''
This function takes a pdf file from the directory or from online to output a txt 
file. The user can specify a specific page or list of pages to extract; otherwise, 
the function extracts text from all pages.
'''
def text(pdf_name: str, pages: Union[int, list] = None, 
                     file_base_name: str = "text"):
  # Checks if pdf file is in directory, downloads if not in directory
  if not exists(pdf_name):
    r = requests.get(pdf_name)
    with open(f"{file_base_name}.pdf", 'wb') as outfile:
      outfile.write(r.content)
    reader = PdfReader(f'{file_base_name}.pdf')
  else:
    reader = PdfReader(pdf_name)
 
  # User wants all images from all pages
  if pages == None:
    for i in range(len(reader.pages)):
      page = reader.pages[i]
      text = page.extract_text()
      with open(f'{file_base_name}.txt', 'a') as f:
        f.write(text)

  # User wants images from one page:
  if type(pages) == int:
    for i in range(len(reader.pages)):
      if i+1 == pages:
        page = reader.pages[i]
        text = page.extract_text()
        with open(f'{file_base_name}.txt', 'a') as f:
          f.write(text)
    
    
  

  # User wants images from list of pages: 
  if type(pages) == list:
    for i in range(len(reader.pages)):
      if i+1 in pages:
        page = reader.pages[i]
        text = page.extract_text()
        with open(f'{file_base_name}.txt', 'a') as f:
          f.write(text)

