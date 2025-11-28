import my_functions as mf
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import xlrd
import numpy as np

salarios = mf.read_json("data/escalas_salariales.json")
cities = mf.read_json("data/cities.json")
muni = mf.read_json("data/municipality_country.json")
abreviaturas = mf.read_json('data/abreviaturas.json')
city = ["HAB", "PRI", "ART", "MAY", "MTZ", "CFG", "VCL", "SSP", "CAV", "CAM", "LTU", "GRM", "HOL", "SCU", "GTM", "IJV"]

def salary(file = salarios):
   for i in range(0,32):
     print(f"{i} | 44 horas: {file['44_horas'][i]} | 40 horas : {file['40_horas'][i]}")

def graph_coin():
  tasas = mf.read_json('data/el_toque.json')

  days = [i for i in range(304)]
  month = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre"]

  usd = [tasas[i]["USD"] for i in tasas]
  euro = [tasas[i]["ECU"] for i in tasas]
  mlc = [tasas[i]["MLC"] for i in tasas]
  usd_oficial = [ 123.6 for _ in usd]

  # Índices del inicio de cada mes (día 0 = 1 de enero)
  inicios = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273]
  
  plt.figure(figsize=(12, 6))
  plt.plot(days[0:304], usd[0:304], label='USD')
  plt.plot(days[0:304], euro[0:304], label = 'EURO')
  plt.plot(days[0:304], mlc[0:304], label = 'MLC')
  # plt.plot(days[0:304], usd_oficial[0:304], label='USD en cadeca')
  plt.xticks(inicios, month, rotation=0)
  plt.title('Comparación del comportamiento del USD, el EURO y el MLC entre enero y octubre de 2025.')
  plt.legend()
  plt.show()

def bar_pymes():
  data = mf.read_json("data/pymes.json")
  count_pymes = [len(mf.list_for_value(data, key='city', value= i.upper().replace(' ',''), second_key='name')) for i in cities ]
  # # provincias =  mf.list_for_value(data,'city') 
  # mpmp = np.array([i.count('MIPYME PRIVADA') for i in types])
  # mpme =  np.array([mf.first_count(i, 'MIPYME ESTATAL') for i in types])
  # cna =  np.array([i.count('COOPERATIVA NO AGROPECUARIA') +  i.count('CNA') for i in types])
  # mipymes_indefinidas = np.array([i.count('MIPYME') for i in types])      
  count_city = np.arange(len(count_pymes))
  # fig , ax = plt.subplots()
  plt.figure(figsize=(14, 6))
  plt.bar(count_city, count_pymes)
  # plt.bar(count_city, mpmp, width=1/5)
  # plt.bar(count_city+0.2,mpme, width=1/5)
  # plt.bar(count_city+0.4,cna, width=1/5)
  # plt.bar(count_city+0.6, mipymes_indefinidas, width=1/5)
  plt.xticks(count_city,city, rotation=0)
  plt.show()





