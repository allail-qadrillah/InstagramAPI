import json
import pandas as pd

def loadFile(fileName, value='username'):
  user = []
  with open(fileName, 'r') as f:
    data = json.load(f)
    
  for i in data:
    user.append(i[value])
    
  return user

def putIntoCSV(namaFile, data):
  pd.DataFrame(data).to_csv(namaFile, index=False)

def putAllIntoCSV(namaFile, **kwargs):
  data = {}
  # dapatkan panjang maksimum dari value kwargs
  max_len = max(len(x) for x in kwargs.values())
  
  for key, value in kwargs.items():
    # untuk array yg pendek replace " " agar panjannya sama
    padded_array = value + [' '] * (max_len - len(value))
    data[key] = padded_array    
    
  # Create a sample DataFrame

  pd.DataFrame(data).to_csv(namaFile, index=False)


  
"""
galuh  18312416545
"""