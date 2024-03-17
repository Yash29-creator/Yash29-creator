#Guide for Pandas
<pre>
import pandas as pd</br>

data = {'Country': ['Belgium',  'India',  'Brazil'],
'Capital': ['Brussels',  'New Delhi',  'Brasilia'],
'Population': [11190846, 1303171035, 207847528]} 
df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])

data = {'Country': ['Belgium',  'India',  'Brazil'],
'Capital': ['Brussels',  'New Delhi',  'Brasilia'],
'Population': [11190846, 1303171035, 207847528]} 
df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])

help(pd.Series.loc)

pd.read_csv('file.csv', header=None, nrows=5)
df.to_csv('myDataFrame.csv')
xlsx = pd.ExcelFile('file.xls')
df = pd.read_excel(xlsx,  'Sheet1')
pd.read_excel('file.xlsx')
df.to_excel('dir/myDataFrame.xlsx',  sheet_name='Sheet1')
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
pd.read_sql(SELECT * FROM my_table;, engine)
pd.read_sql_table('my_table', engine)
pd.read_sql_query(SELECT * FROM my_table;', engine)
df.to_sql('myDf', engine)

s['b']
  -5
df[1:]
  Country     Capital   Population
  1  India    New Delhi 1303171035
  2  Brazil   Brasilia  207847528

df.iloc([0], [0])
  'Belgium'
df.iat([0], [0])
  'Belgium'

df.loc([0],  ['Country'])
  'Belgium'
df.at([0],  ['Country'])
  'Belgium'

df.ix[2]
  Country      Brazil
  Capital    Brasilia
  Population  207847528

df.ix[:, 'Capital']
  0     Brussels
  1    New Delhi
  2     Brasilia

df.ix[1, 'Capital']
  'New Delhi'

s[~(s > 1)]
s[(s < -1) | (s > 2)]
df[df['Population']>1200000000]

s['a'] = 6
df.drop('Country', axis=1) 
df.sort_index()
df.sort_values(by='Country')
df.rank()

df.shape
df.index
df.columns
df.info()
df.count()

df.sum()
df.cumsum()
df.min()/df.max()
df.idxmin()/df.idxmax() 
df.describe()
df.mean()
df.median()

f = lambda x: x*2
df.apply(f)
df.applynap(f) 
s3 = pd.Series([7, -2, 3],  index=['a',  'c',  'd'])
s + s3
  a     10.0
  b     NaN
  c     5.0
  d     7.0

s.add(s3, fill_value=0)
  a    10.0
  b    -5.0
  c    5.0
  d    7.0
s.sub(s3, fill_value=2)
s.div(s3, fill_value=4)
s.mul(s3, fill_value=3)
  
</pre>
