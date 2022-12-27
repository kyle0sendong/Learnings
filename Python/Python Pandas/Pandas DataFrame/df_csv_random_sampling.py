# sample(frac=0.3,random_state=69)
import pandas as pd

insurance = pd.DataFrame(pd.read_csv('insurance.csv')).sample(frac=0.3, random_state=69)