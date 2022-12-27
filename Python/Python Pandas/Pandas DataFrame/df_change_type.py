import pandas as pd

insurance = pd.DataFrame(pd.read_csv("Python\csv_files\insurance.csv"))

insurance['sex'] = insurance['sex'].astype('category')
insurance['smoker'] = insurance['smoker'].astype('category')
insurance['region'] = insurance['region'].astype('category')

