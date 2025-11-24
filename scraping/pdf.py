from PyPDF2 import PdfReader
import pdfplumber
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import my_functions as mf

cities = mf.read_json('../data/cities.json')

def formate_pyme(lista:list) ->bool:
  if lista[2].strip() in cities and type(mf.you_type(lista[0])) == int:
    return True
  return False

mipymes = []
with pdfplumber.open('../sources/Listado de Nuevos Actores Económicos aprobados hasta 09.05.24 .pdf') as pdf:
  count_page = len(pdf.pages)
  # mipymes = actores.pages[0].extract_text().strip().split('\n')
  mipymes = [ mf.del_salto(i) for i in mipymes if formate_pyme(i)]
  mipymes = pdf.pages[9].extract_table()
  print(len(mipymes))
  print(count_page)

name = []

