from PyPDF2 import PdfReader

with open('../sources/Listado de Nuevos Actores Económicos aprobados hasta 09.05.24 .pdf', 'rb') as pdf:
  actores = PdfReader(pdf)
  print(actores.pages[0].extract_text())



