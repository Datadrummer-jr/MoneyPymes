import my_functions as mf
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import xlrd
import numpy as np

salarios = mf.read_json("data/escalas_salariales.json")
cities = mf.read_json("data/cities.json")
   
def salary(file = salarios):
   for i in range(0,32):
     print(f"{i} | 44 horas: {file['44_horas'][i]} | 40 horas : {file['40_horas'][i]}")

def bar_pymes():
  data = mf.read_json("data/pymes.json")
  subject = [ s['subject'] for s in data.values()]
  provincias = [ c['city'] for c in data.values()]
  mpmp = subject.count('MIPYME PRIVADA')
  mpme =  subject.count('MIPYME ESTATAL')
  cna =  subject.count('COOPERATIVA NO AGROPECUARIA') +  subject.count('CNA')
  city = [provincias.count(i) for i in cities]
  count_subject = np.arange(len(city))

bar_pymes()


