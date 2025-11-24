from PyPDF2 import PdfReader
import pdfplumber
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import my_functions as mf

cities = mf.read_json('../data/cities.json')

def formate_pyme(lista:list) ->bool:
  if (lista[2] in cities or lista[2] in mf.read_json('../data/abreviaturas.json')) and str(lista[0]).isdigit():
    return True
  return False

mipymes = []
with pdfplumber.open('../sources/Listado de Nuevos Actores Económicos aprobados hasta 09.05.24 .pdf') as pdf:
  count_page = len(pdf.pages)
  # mipymes = actores.pages[0].extract_text().strip().split('\n')
  mipymes = pdf.pages[8].extract_table()
  mipymes = [ mf.del_salto(i) for i in mipymes if formate_pyme(i)]

def save_pyme(index: int):
  with pdfplumber.open('../sources/Listado de Nuevos Actores Económicos aprobados hasta 09.05.24 .pdf') as pdf:
    mipymes = pdf.pages[index].extract_table()
    indices = []
    name = []
    city = []
    type = []
    activity = []
    mipymes = [ mf.del_salto(i) for i in mipymes if formate_pyme(i)]
    count = len(mipymes)
    indices.extend([ i[0] for i in mipymes])
    name.extend([ n[1] for n in mipymes])
    city.extend([ c[2] for c in mipymes])
    type.extend([ t[-2] for t in mipymes])
    activity.extend([ a[-1] for a in mipymes])
    mipymes_actuales = mf.read_json('../data/count_pymes.json')
    for i in range(count):
      mipymes_actuales[indices[i]] = {'name': name[i], 'city':city[i], 'subject': type[i].upper(), 'activity':activity[i] }
    mf.save_json(mipymes_actuales,'../data/count_pymes.json')
    
if __name__ == '__main__':
  save_pyme(0)