import pdfplumber
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import my_functions as mf

cities = mf.read_json('../data/cities.json')
abreviaturas = mf.read_json('../data/abreviaturas.json')
municipios_por_provincia = mf.read_json('../data/municipality_country.json')
mipymes_actuales = mf.read_json('../data/pymes.json')
rute_pymes = '../sources/Listado de Nuevos Actores Económicos aprobados hasta 09.05.24 .pdf'

def formate_pyme(lista:list) ->bool:
  if str(lista[0]).isdigit()  :
    return True
  return False

def save_pyme(index: int):
  with pdfplumber.open(rute_pymes) as pdf:
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

    for i in range(count):
      if len(city[i]) > 3:
       mipymes_actuales[indices[i]] = {'name': name[i], 'city':city[i], 'subject': type[i].upper(), 'activity':activity[i] }
      else:
        mipymes_actuales[indices[i]] = {'name': name[i], 'city': abreviaturas[str(city[i]).upper()], 'subject': str(type[i]).upper(), 'activity':activity[i] }
  
    ausentes = [ str(i) for i in range(1, max([int(i) for i in mipymes_actuales])+1) if str(i) not in mipymes_actuales]
    mipymes = pdf.pages[index].extract_text().split('\n')
    mipymes = [ i for i in mipymes if formate_pyme(i.split()) and i.split()[0] in ausentes]
    for pyme in mipymes:
      dicc = mf.pymes_parser(pyme,municipios_por_provincia)
      mipymes_actuales[dicc[0]] = dicc[1]
    
    mf.save_json(mipymes_actuales,'../data/pymes.json')
    
if __name__ == '__main__':
  for i in range(len(pdfplumber.open(rute_pymes).pages)):
    save_pyme(i)
  pass