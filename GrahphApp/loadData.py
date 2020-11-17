import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/Abo Samra/Desktop/Django_lectures/GraphQl/db.sqlite3')
df = pd.read_csv('/Users/Abo Samra/Downloads/Compressed/ExcelDjangoGraphQL-master/sam.csv')
df['id'] = df.index
df = df [['id','Segment', 'Country', 'Product', 'Units', 'Sales', 'Datesold']]
df.to_sql('GrahphApp_productmodel' ,conn , if_exists='replace', index=False)